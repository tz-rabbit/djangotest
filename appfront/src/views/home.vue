<template>
  <div>
    <h1>这是home</h1>
    <hr />
    <h2>显示state:{{this.$store.state.name}}</h2>
    <el-button @click="change1">修改默认李四</el-button>
    <el-button @click="change1a">异步修改默认李四</el-button>
    <el-button @click="change1b">getter李四</el-button>

    <el-input v-model="name"></el-input>
    <el-button @click="change2">修改输入</el-button>
    <el-button @click="change2a">异步修改输入</el-button>
    <el-button @click="change2b">getters输入</el-button>
    <hr />

    <el-button @click="test">跳转home2</el-button>
  </div>
</template>
<script>
export default {
  name: "home",
  data() {
    return {
      name: ""
    };
  },
  created() {
    console.log("这是home");
  },
  mounted() {
    console.log("初始");
  },
  methods: {
    test() {
      this.$router.push("/home2");
    },
    change1() {
      this.$store.commit("change1");
      console.log("换李四", this.$store.state.name);
    },
    change2() {
      // this.$store.commit("change2", { name: this.name }); //两种写法都可以
      this.$store.commit({ type: "change2", name: this.name });

      console.log("换input", this.$store.state.name);
    },
    change1a() {
      this.$store.dispatch("change1a");
    },
    change2a() {
      this.$store.dispatch("change2a", { name: this.name });
    },
    change1b() {
      console.log(this.$store.getters.change1b);
    },
    change2b() {
      console.log(this.$store.getters.change2b("是输入的值"));

    }
  }
};
</script>