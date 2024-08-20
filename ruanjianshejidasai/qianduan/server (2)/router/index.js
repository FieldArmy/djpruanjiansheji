import Vue from "vue";
import VueRouter from "vue-router";
import CheckSchool from "@/components/Check/CheckSchool";
import CheckMajor from "@/components/Check/CheckMajor";
import Fillvolunteer from "@/components/Check/Fillvolunteer";
import FillSpring from "@/components/Check/FillSpring";
import int from "@/components/int";

import Opinion from "@/components/Opinion";
import teacher from "@/components/teacher";
import checkschoolMain from "@/components/checkschoolMain";
import schoolTable from "@/components/schoolTable";
import Error from "../src/Views/404";
import teacher_inform from "../src/Views/teacher_inform";
import consult_teacher from "../src/Views/consult_teacher";
import consult_student from "../src/Views/consult_student";

import Main_one from "@/Main/Main_one";
import Administrators from "@/Main/Administrators";

import Admain from "@/Information/Admain";
import useropinion from "@/Information/useropinion";
import tableinfo from "@/Information/tableinfo";
import Collection from "@/Information/Collection";
import TeacherInfo from "../src/Information/TeacherInfo"
import hot_info from "../src/Information/hot_info"

import Bi from "@/components/Bi";

import Login from "../src/Login/Login";
import Login_root from "../src/Login/Login_root";
import Login_Teacher from "../src/Login/Login_Teacher";
import TeaLogin from "@/Login/Tea_register";

import Major_form from "../src/text_tab/Major_form"
import Major_tab from "../src/text_tab/Major_tab"
import Intellect_inner from "../src/text_tab/Intellect_inner"

import Email from "@/Login/components/email";
import ForgetPassword from "@/Login/components/ForgetPassword";
import ChangePass from "@/Login/components/changePass";
import Tea_ChangePass from "../src/Login/components/Tea_ChangePass"
import Tea_ForgetPass from "../src/Login/components/Tea_ForgetPass"

import HomePage from "../src/Views/Index";
import  AI from '../src/Views/AI.vue'
import web1 from "@/components/web/web1";
import web2 from "@/components/web/web2";
import web3 from "@/components/web/web3";
import web4 from "@/components/web/web4";
import web5 from "@/components/web/web5";
import web6 from "@/components/web/web6";


import phone_main from "../src/phone/phone_main";
import phone_home from "../src/phone/phone_home";
import phone_teacher from "../src/phone/phone_teacher";
import phone_checkMajor from "../src/phone/phone_checkMajor";
import phone_MajorSpring from "../src/phone/phone_MajorSpring";
import phone_checkSchool from "../src/phone/phone_checkSchool";
import phone_chooseMajor from "../src/phone/phone_chooseMajor";
import phone_opinion from "../src/phone/phone_opinion";

import phone_web_1 from "../src/phone/phone_web_1";
import phone_web_2 from "../src/phone/phone_web_2";
import phone_web_3 from "../src/phone/phone_web_3";
import phone_web_4 from "../src/phone/phone_web_4";
import phone_web_5 from "../src/phone/phone_web_5";
import phone_web_6 from "../src/phone/phone_web_6";


import VueCookies from 'vue-cookies';

Vue.use(VueCookies);
Vue.use(VueRouter);


const routes = [
    {
        path: "/", name: "login", component: Login, //登录
    },
    {
        path: "/main_one", name: "main_one", component: Main_one,//主菜单
        children: [
            {path: '/index', name: "homePage", component: HomePage,},// 首页轮播图
            {path: '/AI', name: "AI", component: AI,},//AI人工智能
            {path: "/checkschool", name: "checkschool", component: CheckSchool,},//查学校
            {path: "/checkmajor", name: "checkmajor", component: CheckMajor,},//查专业
            {
                path:'/Major_tab',
                component:Major_tab,
                children:[
                    {
                        path: '/Fill',
                        components: {
                            default:Major_tab,
                            // 手动填报
                            fil:Fillvolunteer,
                            // 自动填报表格
                            intell:Intellect_inner,
                            // 志愿表
                            fom:Major_form,
                        }
                    }
                ]
            },

            {path: '/fillspring', name: "fillspring", component: FillSpring,}, //春考填志愿
            {path: "/opinion", name: "opinion", component: Opinion,},//意见反馈
            {path: "/teacher", name: "teacher", component: teacher,},//咨询师
            {path: "/Collection", name: "Collection", component: Collection,},//个人收藏
            {
                path:'/contrast',
                component: () => import('../src/Information/Contrast')
            }
        ]
    },
    {
        path:'/phone_main',
        component:phone_main,
        children:[
            {path:'/phone_home',component:phone_home},
            {path:'/phone_teacher',component:phone_teacher},
            {path:'/phone_zhiyuan',component:phone_chooseMajor},
            {path:'/phone_spring',component:phone_MajorSpring},
            {path:'/phone_major',component:phone_checkMajor},
            {path:'/phone_school',component:phone_checkSchool},
            {path:'/phone_opinion',component:phone_opinion},
        ]
    },
    {path:'/web_1', component:phone_web_1},
    {path:'/web_2', component:phone_web_2},
    {path:'/web_3', component:phone_web_3},
    {path:'/web_4', component:phone_web_4},
    {path:'/web_5', component:phone_web_5},
    {path:'/web_6', component:phone_web_6},
//管理员界面
    {
        path: '/administrators', name: "administrators", component: Administrators,  //管理员
        children: [
            {path: '/Admain', name: "Admain", component: Admain,}, //管理员界面
            {path: '/teacherinfo', name: "teacherinfo", component: TeacherInfo,}, //咨询师界面
            {path: '/useropinion', name: "useropinion", component: useropinion,}, //反馈意见界面
            {path: '/tableinfo', name: "tableinfo", component: tableinfo,}, //折线图
            {path: "/hot_info", name: "hot_info", component: hot_info,},//用户热地图
        ]
    },
    //咨询师主界面
    {
        path: '/consult_teacher', name: "consult_teacher", component: consult_teacher,
        children: [
            {path: '/consult_student', name: "consult_student", component: consult_student,}, //管理员界面
            {path: '/teacher_inform', name: "teacher_inform", component: teacher_inform,}, //管理员界面
        ]
    },
    {
        path: '/checkschoolMain', component: checkschoolMain, children:
            [{path: '/int', name: "int", components: {default: checkschoolMain, ino: int, scl: schoolTable}},]
    },
    {path: '/web1', name: "web1", component: web1,},
    {path: '/web2', name: "web2", component: web2,},
    {path: '/web3', name: "web3", component: web3,},
    {path: '/web4', name: "web4", component: web4,},
    {path: '/web5', name: "web5", component: web5,},
    {path: '/web6', name: "web6", component: web6,},

    {path: "/forgetpassword", name: "forgetpassword", component: ForgetPassword,},//忘记密码
    {path: "/changePass", name: "changePass", component: ChangePass,},//修改密码
    {path: "/email", name: "email", component: Email,},//邮箱
    {path: "/tealogin", name: "tealogin", component: TeaLogin,},//教师注册
    {path: "/login_root", name: "login_root", component: Login_root,},//测试
    {path: "/login_teacher", name: "login_teacher", component: Login_Teacher,},//咨询师登录
    {path: "/Tea_ChangePass", name: "Tea_ChangePass", component: Tea_ChangePass,},//咨询师修改密码
    {path: "/Tea_ForgetPass", name: "Tea_ForgetPass", component: Tea_ForgetPass,},//咨询师忘记密码
    {path: '/Bi', name: "Bi", component: Bi,}, //专业详情页
    {path: '*', name: "Error", component: Error,}, //专业详情页
]
const router = new VueRouter({
    mode:'hash',
    routes
})
//路由守卫
router.beforeEach((to, from, next) => {

    // 记得解开！！！
    if (to.path == '/' || to.path == '/forgetpassword'|| to.path == '/Tea_ForgetPass' || to.path == '/Login_Teacher' ||
        to.path == '/logintext' || to.path == '/email' || to.path == '/login_root' || to.path == '/tealogin' || to.path == '/error') return next();

    const flagStr = window.sessionStorage.getItem("user");
    if (!flagStr) return next('/');
    next();
})

export default router
