<template>
  <div>
    <v-card
    :active="isActive"
    :color="color"
    class="ma-1"
    :class="isActive? 'darken-5 white--text' : 'lighten-5'"
    :elevation="isActive? 24 : 3"
    max-height="77"
    @click="selectClass"
    >
    <v-row>
      <v-col class="ml-1">
        <p>class {{ classIndex }}</p>
      </v-col>
      <v-col>
        <p>{{ numSamples }} samples</p>
      </v-col>
      <v-col>

        <v-btn small class="red white--text" @click="removeClass">delete</v-btn>
      </v-col>
    </v-row>
    </v-card>
  </div>
</template>

<script>
import { inputspaceComputed } from '@/store/helpers'
export default {
  name: "classCard",
  props: {
    classIndex: {
      type: Number
    },
    color: {
        type: String
    }
  },
  data() {
    return {
    };
  },
  methods: {
    removeClass() {
      this.$store.commit("removeClass", this.classIndex);
    },
    selectClass() {
        this.$store.commit("selectClass", this.classIndex-1)
    }
  },
  mounted() {
      this.selectClass()
  },
  destroyed () {
      this.$store.state.currentClass = {};
  },
  computed: {
    ...inputspaceComputed,
      isActive() {
          return this.currentClassIndex == this.classIndex ? true : false
      },
      numSamples() {
        return this.$store.state.classes[this.classIndex - 1].points.length
      }
  },
};
</script>