<template>
  <div>
    <v-card height="600">
      <v-card-actions>
        <v-btn @click="addClass">add class</v-btn>
      </v-card-actions>
      <classCard
        v-for="cls in classes"
        :key="cls.index"
        :classIndex="cls.index"
        :color="cls.color"
      ></classCard>
    </v-card>
  </div>
</template>

<script>
import classCard from "@/components/classification/class-card";
import {  } from "@/store/helpers";
export default {
  name: "classDefinition",
  components: {
    classCard
  },
  data() {
    return {};
  },
  props: {
    classes: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    addClass() {
      if (this.classes.length < 6) {
        this.$store.commit("addClass");
      }
    },
  }
};
</script>