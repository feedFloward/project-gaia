<template>
  <div>
    <v-row>
      <v-col>
        <v-select :items="varianceList" label="brush size" v-model="variance" dense></v-select>
      </v-col>
      <v-col>
        <v-btn color="red white--text" @click="clearClasses" dense>clear canvas</v-btn>
      </v-col>
      <v-col></v-col>
    </v-row>
    <v-row>
      <v-card width="inputspaceWidth" height="inputspaceHeight">
        <canvas
          ref="inputspace_canvas"
          @mousedown="drawMode = true"
          @mouseup="drawMode = false"
          @mouseout="drawMode = false"
          @mousemove="brushPoints"
        ></canvas>
      </v-card>
    </v-row>
  </div>
</template>



<script>
import * as tf from "@tensorflow/tfjs";
import { colorMap } from "@/shared";
export default {
  name: "inputspaceCanvas",
  data() {
    return {
      inputspaceHeight: undefined,
      inputspaceWidth: undefined,
      drawMode: false,
      variance: 7,
      varianceList: [
        { text: "none", value: 0 },
        { text: "low", value: 3 },
        { text: "medium", value: 7 },
        { text: "high", value: 15 }
      ]
    };
  },
  methods: {
    brushPoints(e) {
      if (
        // zweite bedingung von hier als getter in helper definieren
        this.drawMode &&
        Object.keys(this.$store.state.currentClass).length > 0
      ) {
        this.context.globalAlpha = 0.7;
        let datapointX = tf.randomNormal([1, 1], e.offsetX, this.variance);
        let datapointY = tf.randomNormal([1, 1], e.offsetY, this.variance);
        datapointX = datapointX.dataSync()[0];
        datapointY = datapointY.dataSync()[0];
        this.$store.commit("addPointsToClass", [datapointX, datapointY]);
        const color = this.$store.state.currentClass.color;
        this.drawSinglePoint(datapointX, datapointY, 3, color);
      }
    },
    drawSinglePoint(x, y, size = 3, color = "Lime") {
      this.context.fillStyle = color;
      this.context.beginPath();
      this.context.arc(x, y, size, 0, 2 * Math.PI, true);
      this.context.fill();
    },
    redrawCanvas() {
      this.context.globalAlpha = 0.7;
      this.context.clearRect(0, 0, this.inputspaceWidth, this.inputspaceHeight);
      const classesData = this.$store.state.classes;
      for (let i = 0; i < classesData.length; i++) {
        for (let j = 0; j < classesData[i].points.length; j++) {
          const point = classesData[i].points[j];
          const color = classesData[i].color;
          this.drawSinglePoint(point[0], point[1], 3, color);
        }
      }
    },
    clearClasses() {
      this.$store.commit("removeAllClasses");
    },
    drawPredictions() {
      this.redrawCanvas();
      this.context.globalAlpha = 0.1;
      const predictions = this.$store.state.clfResponse.Z;
      for (let i = 0; i < predictions.length; i++) {
        for (let j = 0; j < predictions[i].length; j++) {
          const prediction = predictions[i][j];
          const color = colorMap[prediction];
          this.drawSinglePoint(j, i, 1, color);
        }
      }
    }
  },
  mounted() {
    this.inputspaceHeight = this.$store.state.inputspace.inputspaceHeight;
    this.inputspaceWidth = this.$store.state.inputspace.inputspaceWidth;
    this.context = this.$refs.inputspace_canvas.getContext("2d");
    this.$refs.inputspace_canvas.width = this.inputspaceWidth;
    this.$refs.inputspace_canvas.height = this.inputspaceHeight;
  },
  computed: {
    numClasses() {
      return this.$store.state.classes.length;
    }
  },
  watch: {
    numClasses: function() {
      this.redrawCanvas();
    }
  }
};
</script>