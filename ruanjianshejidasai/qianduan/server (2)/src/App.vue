<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<script>

export default {
  name: 'App',
}
</script>

<style>
body {
  margin: 0;
  overflow: auto !important;
  padding-right: 0 !important;
    background-repeat: no-repeat;
}

#app {
    margin: 0;
    padding: 0;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /*text-align: center;*/
    color: #2c3e50;
}

.el-message-box .el-message-box__title {
    font-weight: 700;
    text-align: center;
}

.el-message-box .el-message-box__message p {
    padding-left: 20px !important;
    line-height: 40px !important;
}

/*以下需要主体添加*/
.el-drawer__header span{
    color: black;
    font-weight: 700;
    text-align: center;
    border: 0;
    box-shadow: transparent;
}

.el-loading-mask.is-fullscreen .el-loading-spinner{
  margin-top: 0!important;
}

.el-loading-spinner .el-loading-text{
  font-size: 20px!important;
}

.el-loading-spinner .circular{
  /*width: 42px;*/
  /*height: 42px;*/
  /*animation: rotating 2s linear infinite;*/
  display: none;
}

.el-loading-spinner{
  /* 图片替换为你自定义的即可 */
  background-image: url('./assets/Loading22.gif');
  background-repeat: no-repeat;
  background-position: center;
  height: 100%;
  top: 0!important;
}
</style>

