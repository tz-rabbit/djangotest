<template>
  <div>
    <h1>这是home2</h1>
  <el-button @click="test">跳转home</el-button>
  </div>
</template>
<script>
export default {
  name: "home2",
    created(){
      console.log("这是home2")
      console.log("name", this.$store.state.name);
      
  },
  methods: {
    test() {
      this.$router.push("/home");
    }
  }
};
</script>