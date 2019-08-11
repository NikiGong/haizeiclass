<template>
  <div class="login">
    <header-component></header-component>
    <div class="login-context">
      <h2>账号登录</h2>

      <el-form label-position="left" :model="loginForm" :rules="rules" ref="loginFormRef" label-width="50px" class="demo-ruleForm">
        <el-form-item label="名称" prop="name">
          <el-input v-model="loginForm.name"  placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="loginForm.password"  placeholder="请输入密码" show-password></el-input>
        </el-form-item>
      </el-form>

      <div>
        <el-button type="success" @click="login">登录</el-button>
        <el-button type="danger" @click="register">注册</el-button>
      </div>
    </div>
  </div>
</template>

<script>
  import header from "../components/header"

  export default {
    name: 'login',
    components:{
      "header-component": header,
    },
    props: {},
    data(){
      return {

        loginForm: {
          name: "",
          password: "",
        },
        rules: {
          name:[
            {required:true, message:'请输入用户名称', trigger:'blur'},
            {min:1, max:30, message:'长度在1到30个字符',trigger:'blur'}
          ],
          password:[
            {required:true, message:'请输入用户密码', trigger:'blur'},
            {min:1, max:30, message:'长度在1到30个字符',trigger:'blur'}
          ],
        },

      }
    },
    methods: {
      validForm() {
        if(this.loginForm.name ==""){
          alert("用户名不能为空！")
        }

        if(this.loginForm.password == "") {
          alert("密码不能为空！")
        }
      },
      login() {
        // console.log(this.$refs.loginFormRef)
        // ref相当于js里面的id
        // 找到ref为loginForm的元素，然后调用校验方法validate
        this.$refs.loginFormRef.validate((valid) => {
          if (valid) {  //代表校验通过
            // alert('校验通过!');
          } else {  //代表校验失败
            // alert('校验失败!');
          }
        });
        // this.validForm()
      },
      register(){
        this.$refs.loginFormRef.validate((valid) => {
          if (valid) {  //代表校验通过
          } else {  //代表校验失败
          }
        });
      },
    },



  }
</script>

<style scoped>
  .login-context{
    width: 400px;
    margin-left: auto ;
    margin-right: auto;
    border-radius: 2px;
    border: 1px solid #a0b1c4;
    margin-top: 50px;

    padding: 10px 30px;
  }


</style>