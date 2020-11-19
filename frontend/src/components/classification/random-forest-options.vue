<template>
  <div>
    <v-slider
    v-model="specs"
    min="1"
    max="200"
    label="number of estimators"
    thumb-label="always"
    :thumb-size="24"
    ></v-slider>
    <span v-if="getNumEstimatorsTree == 1">This is basicaly a decision tree trained on a random dataset...</span>
  </div>
</template>


<script lang="ts">
import Vue from 'vue';
import { randomForestMethods, randomForestComputed } from "../../store/helpers"; // ts config oder so anpassen damit @/store.. funktioniert
export default Vue.extend({
  name: "randomForestOptions",
  data() {
    return {

    }
  },
  methods: {
    ...randomForestMethods,
  },

  computed: {
    // das so nochmal überdenken, WENN MÖGLICH IN HELPERS AUSLAGERN!!!!
    ...randomForestComputed,
    
    specs: {
      get(): number {
        return this.getNumEstimatorsTree;
      },
      set(numEstimators: number) {
        this.rfChooseNumEst(numEstimators);
      }
    },
  }
});
</script>