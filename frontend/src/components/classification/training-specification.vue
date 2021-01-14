<template>
    <div>
    <v-row align="end">
      <v-col>
        <v-slider
          v-model="trainTestSplit"
          min="0.05"
          max="0.5"
          step="0.01"
          label="test/train-split"
          thumb-label="always"
        ></v-slider>
      </v-col>
    </v-row>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { trainingSpecsComputed } from '@/store/helpers';
export default Vue.extend({
  name: 'trainingSpecification',
  data() {
    return {
      // specs: ''
    }
  },
  computed: {
    trainTestSplit: {
      get() {
        return this.$store.state.trainingSpecs.test_size;
      },
      set(trainTestSplit) {
        this.setTrainTestSplit(trainTestSplit);
      }
    }
  },
  methods: {
    ...trainingSpecsComputed
  },
});
</script>