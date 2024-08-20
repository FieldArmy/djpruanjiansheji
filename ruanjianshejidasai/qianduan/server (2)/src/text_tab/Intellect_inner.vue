<template>
  <div id="card" style="background-color: white">
    <h4>院校地区</h4>
    <el-cascader
        placeholder="不限"
        :options="options1"
        filterable
        v-model="mod_add"
        clearable
        collapse-tags
        :props="{ multiple: true, expandTrigger: 'hover' }"
    >
    </el-cascader>

    <h4>院校类型</h4>
    <el-cascader
        placeholder="不限"
        :options="options4"
        filterable
        v-model="mod_sch_style"
        clearable
        collapse-tags
        :props="{ multiple: true, expandTrigger: 'hover' }"
    >
    </el-cascader>

    <h4>填报批次</h4>
    <el-radio-group v-model="radio">
      <el-radio-button label="本科" :disabled="disMajor(mark)">本科</el-radio-button>
      <el-radio-button label="专科">专科</el-radio-button>
    </el-radio-group>

    <h4>专业意向</h4>
    <el-cascader
        v-if="(Major_show(radio) == 1)?true:false"
        placeholder="不限"
        :options="options2"
        filterable
        v-model="mod_major_ben"
        clearable
        collapse-tags
        :props="{ multiple: true, expandTrigger: 'hover' }"
    >
    </el-cascader>
    <el-cascader
        v-if="(Major_show(radio) == 2)?true:false"
        placeholder="不限"
        :options="options3"
        filterable
        v-model="mod_major_zhuan"
        clearable
        collapse-tags
        :props="{ multiple: true, expandTrigger: 'hover' }"
    >
    </el-cascader>

    <div id="switch-box">
      <h4>是否允许系统自动推荐？</h4>
      <span class="switch-tit">否</span>
      <el-switch v-model="button_flag" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
      <span class="switch-tit">是</span>
    </div>

    <br>
    <el-button type="primary" style="margin-top: 15px" @click="giveData">点击生成</el-button>
  </div>
</template>

<script>
export default {
  name: "Intellect_inner",
  data(){
    return{
      user_name:'',

      mod_add:"*",
      mod_sch_style:"*",
      radio:'本科',
      mod_major_ben:"*",
      mod_major_zhuan:"*",
      button_flag:true,

      mark:null,

      //地区
      options1: [
        {value: '-北京市', label: '北京市',},
        {value: '-天津市', label: '天津市',},
        {
          value: '+山东', label: '山东省',
          children: [
            {value: '-济南市', label: '济南市'},
            {value: '-青岛市', label: '青岛市'},
            {value: '-淄博市', label: '淄博市'},
            {value: '-枣庄市', label: '枣庄市'},
            {value: '-东营市', label: '东营市'},
            {value: '-临沂市', label: '临沂市'},
            {value: '-烟台市', label: '烟台市'},
            {value: '-潍坊市', label: '潍坊市'},
            {value: '-济宁市', label: '济宁市'},
            {value: '-泰安市', label: '泰安市'},
            {value: '-威海市', label: '威海市'},
            {value: '-日照市', label: '日照市'},
            {value: '-莱芜市', label: '莱芜市'},
            {value: '-德州市', label: '德州市'},
            {value: '-聊城市', label: '聊城市'},
            {value: '-菏泽市', label: '菏泽市'},
            {value: '-滨州市', label: '滨州市'},
          ]
        },
        {
          value: '+河北', label: '河北省',
          children: [
            {value: '-石家庄市', label: '石家庄市'},
            {value: '-唐山市', label: '唐山市'},
            {value: '-秦皇岛市', label: '秦皇岛市'},
            {value: '-邯郸市', label: '邯郸市'},
            {value: '-邢台市', label: '邢台市'},
            {value: '-保定市', label: '保定市'},
            {value: '-张家口市', label: '张家口市'},
            {value: '-承德市', label: '承德市'},
            {value: '-沧州市', label: '沧州市'},
            {value: '-廊坊市', label: '廊坊市'},
          ]
        },
        {
          value: '+山西', label: '山西省',
          children: [
            {value: '-太原市', label: '太原市'},
            {value: '-大同市', label: '大同市'},
            {value: '-阳泉市', label: '阳泉市'},
            {value: '-长治市', label: '长治市'},
            {value: '-晋城市', label: '晋城市'},
            {value: '-朔州市', label: '朔州市'},
            {value: '-晋中市', label: '晋中市'},
            {value: '-运城市', label: '运城市'},
            {value: '-忻州市', label: '忻州市'},
            {value: '-临汾市', label: '临汾市'},
            {value: '-吕梁市', label: '吕梁市'},
          ]
        },
        {
          value: '+河南', label: '河南省',
          children: [
            {value: '-郑州市', label: '郑州市'},
            {value: '-开封市', label: '开封市'},
            {value: '-洛阳市', label: '洛阳市'},
            {value: '-平顶山市', label: '平顶山市'},
            {value: '-安阳市', label: '安阳市'},
            {value: '-新乡市', label: '新乡市'},
            {value: '-鹤壁市', label: '鹤壁市'},
            {value: '-焦作市', label: '焦作市'},
            {value: '-濮阳市', label: '濮阳市'},
            {value: '-许昌市', label: '许昌市'},
            {value: '-漯河市', label: '漯河市'},
            {value: '-三门峡市', label: '三门峡市'},
            {value: '-南阳市', label: '南阳市'},
            {value: '-商丘市', label: '商丘市'},
            {value: '-信阳市', label: '信阳市'},
            {value: '-周口市', label: '周口市'},
            {value: '-驻马店市', label: '驻马店市'},
            {value: '-济源市', label: '济源市'},
          ]
        },
        {
          value: '+内蒙古', label: '内蒙古',
          children: [
            {value: '-呼和浩特市', label: '呼和浩特市'},
            {value: '-包头市', label: '包头市'},
            {value: '-乌海市', label: '乌海市'},
            {value: '-赤峰市', label: '赤峰市'},
            {value: '-通辽市', label: '通辽市'},
            {value: '-鄂尔多斯', label: '鄂尔多斯市'},
            {value: '-呼伦贝尔', label: '呼伦贝尔市'},
            {value: '-巴彦淖尔', label: '巴彦淖尔市'},
            {value: '-乌兰察布', label: '乌兰察布市'},
            {value: '-阿拉善盟', label: '阿拉善盟'},
            {value: '-乌兰浩特', label: '乌兰浩特市'},
            {value: '-锡林浩特', label: '锡林浩特市'},
            {value: '-兴安盟', label: '兴安盟'},

          ]
        },
        {
          value: '+湖北', label: '湖北省',
          children: [
            {value: '-武汉市', label: '武汉市'},
            {value: '-黄石市', label: '黄石市'},
            {value: '-十堰市', label: '十堰市'},
            {value: '-宜昌市', label: '宜昌市'},
            {value: '-襄阳市', label: '襄阳市'},
            {value: '-鄂州市', label: '鄂州市'},
            {value: '-荆门市', label: '荆门市'},
            {value: '-孝感市', label: '孝感市'},
            {value: '-荆州市', label: '荆州市'},
            {value: '-黄冈市', label: '黄冈市'},
            {value: '-咸宁市', label: '咸宁市'},
            {value: '-随州市', label: '随州市'},
            {value: '-仙桃市', label: '仙桃市'},
            {value: '-天门市', label: '天门市'},
            {value: '-潜江市', label: '潜江市'},
            {value: '-恩施市', label: '恩施市'},
          ]
        },
        {
          value: '+辽宁', label: '辽宁省',
          children: [
            {value: '-沈阳市', label: '沈阳市'},
            {value: '-大连市', label: '大连市'},
            {value: '-鞍山市', label: '鞍山市'},
            {value: '-抚顺市', label: '抚顺市'},
            {value: '-本溪市', label: '本溪市'},
            {value: '-丹东市', label: '丹东市'},
            {value: '-锦州市', label: '锦州市'},
            {value: '-营口市', label: '营口市'},
            {value: '-阜新市', label: '阜新市'},
            {value: '-辽阳市', label: '辽阳市'},
            {value: '-盘锦市', label: '盘锦市'},
            {value: '-铁岭市', label: '铁岭市'},
            {value: '-朝阳市', label: '朝阳市'},
            {value: '-葫芦岛市', label: '葫芦岛市'},
          ]
        },
        {
          value: '+吉林', label: '吉林省',
          children: [
            {value: '-长春市', label: '长春市'},
            {value: '-吉林市', label: '吉林市'},
            {value: '-四平市', label: '四平市'},
            {value: '-辽源市', label: '辽源市'},
            {value: '-通化市', label: '通化市'},
            {value: '-白山市', label: '白山市'},
            {value: '-松原市', label: '松原市'},
            {value: '-白城市', label: '白城市'},
            {value: '-延吉市', label: '延吉市'},
            {value: '-龙井市', label: '龙井市'},

          ]
        },
        {
          value: '+黑龙江', label: '黑龙江省',
          children: [
            {value: '-哈尔滨市', label: '哈尔滨市'},
            {value: '-齐齐哈尔市', label: '齐齐哈尔市'},
            {value: '-鸡西市', label: '鸡西市'},
            {value: '-鹤岗市', label: '鹤岗市'},
            {value: '-双鸭山市', label: '双鸭山市'},
            {value: '-大庆市', label: '大庆市'},
            {value: '-伊春市', label: '伊春市'},
            {value: '-佳木斯市', label: '佳木斯市'},
            {value: '-七台河市', label: '七台河市'},
            {value: '-牡丹江市', label: '牡丹江市'},
            {value: '-黑河市', label: '黑河市'},
            {value: '-绥化市', label: '绥化市'},
            {value: '-大兴安岭地区', label: '大兴安岭地区'},

          ]
        },
        {value: '-上海', label: '上海市'},
        {
          value: '+江苏', label: '江苏省',
          children: [
            {value: '-南京市', label: '南京市'},
            {value: '-无锡市', label: '无锡市'},
            {value: '-徐州市', label: '徐州市'},
            {value: '-常州市', label: '常州市'},
            {value: '-苏州市', label: '苏州市'},
            {value: '-南通市', label: '南通市'},
            {value: '-连云港市', label: '连云港市'},
            {value: '-淮安市', label: '淮安市'},
            {value: '-盐城市', label: '盐城市'},
            {value: '-扬州市', label: '扬州市'},
            {value: '-镇江市', label: '镇江市'},
            {value: '-泰州市', label: '泰州市'},
            {value: '-宿迁市', label: '宿迁市'},
            {value: '-张家港市', label: '张家港市'},
            {value: '-昆山市', label: '昆山市'},
          ]
        },
        {
          value: '+浙江', label: '浙江省',
          children: [
            {value: '-杭州市', label: '杭州市'},
            {value: '-宁波市', label: '宁波市'},
            {value: '-温州市', label: '温州市'},
            {value: '-嘉兴市', label: '嘉兴市'},
            {value: '-湖州市', label: '湖州市'},
            {value: '-绍兴市', label: '绍兴市'},
            {value: '-金华市', label: '金华市'},
            {value: '-衢州市', label: '衢州市'},
            {value: '-舟山市', label: '舟山市'},
            {value: '-台州市', label: '台州市'},
            {value: '-丽水市', label: '丽水市'},
          ]
        },
        {
          value: '+安徽', label: '安徽省',
          children: [
            {value: '-合肥市', label: '合肥市'},
            {value: '-芜湖市', label: '蚌埠市'},
            {value: '-蚌埠市', label: '蚌埠市'},
            {value: '-淮南市', label: '淮南市'},
            {value: '-马鞍山市', label: '马鞍山市'},
            {value: '-淮北市', label: '淮北市'},
            {value: '-铜陵市', label: '铜陵市'},
            {value: '-安庆市', label: '安庆市'},
            {value: '-黄山市', label: '黄山市'},
            {value: '-滁州市', label: '滁州市'},
            {value: '-阜阳市', label: '阜阳市'},
            {value: '-宿州市', label: '宿州市'},
            {value: '-六安市', label: '六安市'},
            {value: '-亳州市', label: '亳州市'},
            {value: '-池州市', label: '池州市'},
            {value: '-宣城市', label: '宣城市'},
          ]
        },
        {
          value: '+福建', label: '福建省',
          children: [
            {value: '-福州市', label: '福州市'},
            {value: '-厦门市', label: '厦门市'},
            {value: '-莆田市', label: '莆田市'},
            {value: '-三明市', label: '三明市'},
            {value: '-泉州市', label: '泉州市'},
            {value: '-漳州市', label: '漳州市'},
            {value: '-南平市', label: '南平市'},
            {value: '-龙岩市', label: '龙岩市'},
            {value: '-宁德市', label: '宁德市'},

          ]
        },
        {
          value: '+江西', label: '江西省',
          children: [
            {value: '-南昌市', label: '南昌市'},
            {value: '-景德镇市', label: '景德镇市'},
            {value: '-萍乡市', label: '萍乡市'},
            {value: '-九江市', label: '九江市'},
            {value: '-新余市', label: '新余市'},
            {value: '-鹰潭市', label: '鹰潭市'},
            {value: '-赣州市', label: '赣州市'},
            {value: '-吉安市', label: '吉安市'},
            {value: '-宜春市', label: '宜春市'},
            {value: '-抚州市', label: '抚州市'},
            {value: '-上饶市', label: '上饶市'},

          ]
        },
        {
          value: '+湖南', label: '湖南省',
          children: [
            {value: '-长沙市', label: '长沙市'},
            {value: '-株洲市', label: '株洲市'},
            {value: '-湘潭市', label: '湘潭市'},
            {value: '-衡阳市', label: '衡阳市'},
            {value: '-邵阳市', label: '邵阳市'},
            {value: '-岳阳市', label: '岳阳市'},
            {value: '-常德市', label: '常德市'},
            {value: '-张家界市', label: '张家界市'},
            {value: '-益阳市', label: '益阳市'},
            {value: '-郴州市', label: '郴州市'},
            {value: '-永州市', label: '永州市'},
            {value: '-怀化市', label: '怀化市'},
            {value: '-娄底市', label: '娄底市'},
            {value: '-湘西市', label: '湘西土家苗族自治州'},
            {value: '-吉首市', label: '吉首市'},
          ]
        },
        {
          value: '+广东', label: '广东省',
          children: [
            {value: '-广州市', label: '广州市'},
            {value: '-韶关市', label: '韶关市'},
            {value: '-深圳市', label: '深圳市'},
            {value: '-珠海市', label: '珠海市'},
            {value: '-汕头市', label: '汕头市'},
            {value: '-佛山市', label: '佛山市'},
            {value: '-江门市', label: '江门市'},
            {value: '-湛江市', label: '湛江市'},
            {value: '-茂名市', label: '茂名市'},
            {value: '-肇庆市', label: '肇庆市'},
            {value: '-惠州市', label: '惠州市'},
            {value: '-梅州市', label: '梅州市'},
            {value: '-汕尾市', label: '汕尾市'},
            {value: '-河源市', label: '河源市'},
            {value: '-阳江市', label: '阳江市'},
            {value: '-清远市', label: '清远市'},
            {value: '-东莞市', label: '东莞市'},
            {value: '-中山市', label: '中山市'},
            {value: '-潮州市', label: '潮州市'},
            {value: '-揭阳市', label: '揭阳市'},
            {value: '-云浮市', label: '云浮市'},
          ]
        },
        {
          value: '+广西', label: '广西省',
          children: [
            {value: '-南宁市', label: '南宁市'},
            {value: '-柳州市', label: '柳州市'},
            {value: '-桂林市', label: '桂林市'},
            {value: '-梧州市', label: '梧州市'},
            {value: '-北海市', label: '北海市'},
            {value: '-钦州市', label: '钦州市'},
            {value: '-贵港市', label: '贵港市'},
            {value: '-玉林市', label: '玉林市'},
            {value: '-百色市', label: '百色市'},
            {value: '-贺州市', label: '贺州市'},
            {value: '-河池市', label: '河池市'},
            {value: '-来宾市', label: '来宾市'},
            {value: '-崇左市', label: '崇左市'},
          ]
        },
        {
          value: '+海南', label: '海南省',
          children: [
            {value: '-海口市', label: '海口市'},
            {value: '-三亚市', label: '三亚市'},
            {value: '-琼海市', label: '琼海市'},
            {value: '-文昌市', label: '文昌市'},
          ]
        },
        {value: '-重庆', label: '重庆市',},
        {
          value: '+四川', label: '四川省',
          children: [
            {value: '-成都市', label: '成都市'},
            {value: '-自贡市', label: '自贡市'},
            {value: '-攀枝花市', label: '攀枝花市'},
            {value: '-泸州市', label: '泸州市'},
            {value: '-德阳市', label: '德阳市'},
            {value: '-绵阳市', label: '绵阳市'},
            {value: '-广元市', label: '广元市'},
            {value: '-遂宁市', label: '遂宁市'},
            {value: '-内江市', label: '内江市'},
            {value: '-乐山市', label: '乐山市'},
            {value: '-南充市', label: '南充市'},
            {value: '-眉山市', label: '眉山市'},
            {value: '-宜宾市', label: '宜宾市'},
            {value: '-广安市', label: '广安市'},
            {value: '-达州市', label: '达州市'},
            {value: '-雅安市', label: '雅安市'},
            {value: '-巴中市', label: '巴中市'},
            {value: '-资阳市', label: '资阳市'},
            {value: '-阿坝市', label: '阿坝藏族羌族自治州'},
            {value: '-康定市', label: '康定市'},
            {value: '-西昌市', label: '西昌市'},
          ]
        },
        {
          value: '+贵州', label: '贵州省',
          children: [
            {value: '-贵阳市', label: '贵阳市'},
            {value: '-六盘水市', label: '六盘水市'},
            {value: '-遵义市', label: '遵义市'},
            {value: '-安顺市', label: '安顺市'},
            {value: '-铜仁市', label: '铜仁市'},
            {value: '-毕节市', label: '毕节市'},
            {value: '-黔南市', label: '黔南布依族苗族自治州'},
            {value: '-兴义市', label: '兴义市'},
            {value: '-凯里市', label: '凯里市'},
            {value: '-福泉市', label: '福泉市'},
            {value: '-都匀市', label: '都匀市'},

          ]
        },
        {
          value: '+云南', label: '云南省',
          children: [
            {value: '-昆明市', label: '昆明市'},
            {value: '-曲靖市', label: '曲靖市'},
            {value: '-玉溪市', label: '玉溪市'},
            {value: '-保山市', label: '保山市'},
            {value: '-昭通市', label: '昭通市'},
            {value: '-丽江市', label: '丽江市'},
            {value: '-临沧市', label: '临沧市'},
            {value: '-普洱市', label: '普洱市'},
            {value: '-个旧市', label: '个旧市'},
            {value: '-大理市', label: '大理市'},
            {value: '-文山市', label: '文山市'},
            {value: '-景洪市', label: '景洪市'},
            {value: '-楚雄市', label: '楚雄市'},
            {value: '-芒市', label: '芒市'},
            {value: '-蒙自市', label: '蒙自市'},
          ]
        },
        {
          value: '+西藏', label: '西藏自治区',
          children: [
            {value: '-拉萨市', label: '拉萨市'},
            {value: '-林芝市', label: '林芝市'},
          ]
        },
        {
          value: '+陕西', label: '陕西省',
          children: [
            {value: '-西安市', label: '西安市'},
            {value: '-铜川市', label: '铜川市'},
            {value: '-宝鸡市', label: '宝鸡市'},
            {value: '-咸阳市', label: '咸阳市'},
            {value: '-渭南市', label: '渭南市'},
            {value: '-延安市', label: '延安市'},
            {value: '-汉中市', label: '汉中市'},
            {value: '-榆林市', label: '榆林市'},
            {value: '-安康市', label: '安康市'},
            {value: '-商洛市', label: '商洛市'},
            {value: '-神木市', label: '神木市'},
          ]
        },
        {
          value: '+甘肃', label: '甘肃省',
          children: [
            {value: '-兰州市', label: '兰州市'},
            {value: '-嘉峪关市', label: '嘉峪关市'},
            {value: '-金昌市', label: '金昌市'},
            {value: '-白银市', label: '白银市'},
            {value: '-天水市', label: '天水市'},
            {value: '-武威市', label: '武威市'},
            {value: '-张掖市', label: '张掖市'},
            {value: '-平凉市', label: '平凉市'},
            {value: '-酒泉市', label: '酒泉市'},
            {value: '-庆阳市', label: '庆阳市'},
            {value: '-定西市', label: '定西市'},
            {value: '-陇南市', label: '陇南市'},
            {value: '-甘南藏市', label: '甘南藏族自治州'},
            {value: '-临夏市', label: '临夏市'},
          ]
        },
        {
          value: '+青海', label: '青海省',
          children: [
            {value: '-西宁市', label: '西宁市'},
            {value: '-海东市', label: '海东市'},
            {value: '-海西市', label: '海西州德令哈市'},
          ]
        },
        {
          value: '+宁夏', label: '宁夏省',
          children: [
            {value: '-银川市', label: '银川市'},
            {value: '-石嘴山市', label: '石嘴山市'},
            {value: '-吴忠市', label: '吴忠市'},
            {value: '-固原市', label: '固原市'},
          ]
        },
        {
          value: '+新疆', label: '新疆自治区',
          children: [
            {value: '-乌鲁木齐市', label: '乌鲁木齐市'},
            {value: '-克拉玛依市', label: '克拉玛依市'},
            {value: '-和田地区', label: '和田地区'},
            {value: '-塔城地区', label: '塔城地区'},
            {value: '-石河子市', label: '石河子市'},
            {value: '-阿拉尔市', label: '阿拉尔市'},
            {value: '-五家渠市', label: '五家渠市'},
            {value: '-吐鲁番市', label: '吐鲁番市'},
            {value: '-哈密市', label: '哈密市'},
            {value: '-伊宁市', label: '伊宁市'},
            {value: '-博乐市', label: '博乐市'},
            {value: '-喀什市', label: '喀什市'},
            {value: '-奎屯市', label: '奎屯市'},
            {value: '-库尔勒市', label: '库尔勒市'},
            {value: '-昌吉市', label: '昌吉市'},
            {value: '-铁门关市', label: '铁门关市'},
            {value: '-阿克苏市', label: '阿克苏市'},
            {value: '-阿勒泰市', label: '阿勒泰市'},
            {value: '-阿图什市', label: '阿图什市'},
          ]
        },
        {value: '-香港', label: '香港特别行政区',},
        {value: '-澳门', label: '澳门特别行政区',},
        {
          value: '+台湾', label: '台湾省',
          children: [
            {value: '-桃园市', label: '桃园市'},
            {value: '-嘉义市', label: '嘉义市'},
            {value: '-台北市', label: '台北市'},
            {value: '-新竹市', label: '新竹市'},
          ]
        },
      ],
      //本科专业
      options2: [
        {
          value: '哲学类', label: '哲学',
          children: [
            {value: '-哲学', label: '哲学类'}
          ]
        },
        {
          value: '经济学', label: '经济学',
          children: [
            {value: '-经济学类', label: '经济学类'},
            {value: '-财政', label: '财政学类'},
            {value: '-金融', label: '金融学类'},
            {value: '-经济与贸易', label: '经济与贸易类'},
          ]
        },
        {
          value: '法学', label: '法学',
          children: [
            {value: '-法学', label: '法学类'},
            {value: '-政治学', label: '政治学类'},
            {value: '-社会学', label: '社会学类'},
            {value: '-民族学', label: '民族学类'},
            {value: '-马克思学', label: '马克思学类'},
            {value: '-公安学', label: '公安学类'},
          ]
        },
        {
          value: '文学', label: '文学',
          children: [
            {value: '-中国语言文学', label: '中国语言文学类'},
            {value: '-外国语言文学', label: '外国语言文学类'},
            {value: '-新闻传播学', label: '新闻传播学类'},
          ]
        },
        {
          value: '教育', label: '教育学',
          children: [
            {value: '-教育学', label: '教育学类'},
            {value: '-体育学', label: '体育学类'},
          ]
        },
        {
          value: '历史学', label: '历史学类',
          children: [
            {value: '-历史', label: '历史类'}
          ]
        },
        {
          value: '理学', label: '理学',
          children: [
            {value: '-数', label: '数学类'},
            {value: '-物理', label: '物理学类'},
            {value: '-化', label: '化学类'},
            {value: '-天文', label: '天文学类'},
            {value: '-地理', label: '地理科学学类'},
            {value: '-大气', label: '大气科学学类'},
            {value: '-海洋', label: '海洋科学学类'},
            {value: '-地球物理', label: '地球物理学类'},
            {value: '-地质', label: '地质学类'},
            {value: '-生物科', label: '生物科学类'},
            {value: '-心理', label: '心理学类'},
            {value: '-统计', label: '统计学类'},
          ]
        },
        {
          value: '工学', label: '工学',
          children: [
            {value: '-力学', label: '力学类'},
            {value: '-机械', label: '机械类'},
            {value: '-仪器', label: '仪器类'},
            {value: '-材料', label: '材料类'},
            {value: '-能源动力', label: '能源动力类'},
            {value: '-电气', label: '电气类'},
            {value: '-电子', label: '电子信息类'},
            {value: '-自动化', label: '自动化类'},
            {value: '-计算机', label: '计算机类'},
            {value: '-土木', label: '土木类'},
            {value: '-水利', label: '水利类'},
            {value: '-测绘', label: '测绘类'},
            {value: '-化工', label: '化工类'},
            {value: '-地质', label: '地质类'},
            {value: '-矿业', label: '矿业类'},
            {value: '-纺织', label: '纺织类'},
            {value: '-轻工', label: '轻工类'},
            {value: '-交通运输', label: '交通运输类'},
            {value: '-海洋工程', label: '海洋工程类'},
            {value: '-航空航天', label: '航空航天类'},
            {value: '-兵器', label: '兵器类'},
            {value: '-核工程', label: '核工程类'},
            {value: '-农业工程', label: '农业工程类'},
            {value: '-林业工程', label: '林业工程类'},
            {value: '-坏境科学与工程', label: '坏境科学与工程类'},
            {value: '-生物医学工程', label: '生物医学工程类'},
            {value: '-食品科学与工程', label: '食品科学与工程类'},
            {value: '-建筑', label: '建筑类'},
            {value: '-安全科学与工程', label: '安全科学与工程类'},
            {value: '-生物工程', label: '生物工程类'},
            {value: '-公安技术', label: '公安技术类'},
          ]
        },
        {
          value: '农学', label: '农学',
          children: [
            {value: '-植物生产', label: '植物生产类'},
            {value: '-自然保护与环境生态', label: '自然保护与环境生态类'},
            {value: '-动物生产', label: '动物生产类'},
            {value: '-动物医学', label: '动物医学类'},
            {value: '-林学', label: '林学类'},
            {value: '-水产', label: '水产类'},
            {value: '-草', label: '草学类'},
          ]
        },
        {
          value: '医学', label: '医学',
          children: [
            {value: '-基础医学', label: '基础医学类'},
            {value: '-临床医学', label: '临床医学类'},
            {value: '-口腔医学', label: '口腔医学类'},
            {value: '-公共卫生', label: '公共卫生与预防学类'},
            {value: '-中医学', label: '中医学类'},
            {value: '-中西医结合', label: '中西医结合类'},
            {value: '-药学', label: '药学类'},
            {value: '-中药学', label: '中药学类'},
            {value: '-法医学', label: '法医学类'},
            {value: '-医学技术', label: '医学技术类'},
            {value: '-护理学', label: '护理学类'},
          ]
        },
        {
          value: '管理', label: '管理学',
          children: [
            {value: '-管理', label: '管理科学与工程类'},
            {value: '-工商管理', label: '工商管理类'},
            {value: '-农业经济管理', label: '农业经济管理类'},
            {value: '-公共管理', label: '公共管理类'},
            {value: '-图书', label: '图书情报与档案管理类'},
            {value: '-物流', label: '物流管理与工程类'},
            {value: '-工业工程', label: '工业工程类'},
            {value: '-电子商务', label: '电子商务类'},
            {value: '-旅游管理', label: '旅游管理类'},
          ]
        },
        {
          value: '艺术学', label: '艺术学',
          children: [
            {value: '-艺术学理论', label: '艺术学理论类'},
            {value: '-音乐与舞蹈学', label: '音乐与舞蹈学类'},
            {value: '-戏剧与影视学', label: '戏剧与影视学类'},
            {value: '-美术学', label: '美术学类'},
            {value: '-设计学', label: '设计学类'},
          ]
        },
      ],
      //专科专业
      options3: [
        {
          value: '农林牧渔', label: '农林牧渔',
          children: [
            {value: '-农业', label: '农业类'},
            {value: '-林业', label: '林业类'},
            {value: '-畜牧', label: '畜牧类'},
            {value: '-渔业', label: '渔业类'},
          ]
        },
        {
          value: '资源', label: '资源环境与安全',
          children: [
            {value: '-资源', label: '资源勘查类'},
            {value: '-地质', label: '地质类'},
            {value: '-测绘', label: '测绘地理信息类'},
            {value: '-石油', label: '石油与天然气类'},
            {value: '-煤炭', label: '煤炭类'},
            {value: '-金属与非金属', label: '金属与非金属类'},
            {value: '-气象', label: '气象类'},
            {value: '-环境保护', label: '环境保护类'},
            {value: '-安全', label: '安全类'},
          ]
        },
        {
          value: '能源动力', label: '能源动力与材料',
          children: [
            {value: '-电力技术', label: '电力技术类'},
            {value: '-热能', label: '热能与发电工程类'},
            {value: '-新能源', label: '新能源发电工程类'},
            {value: '-金属', label: '黑色金属材料类'},
            {value: '-材料', label: '有色金属材料类'},
            {value: '-非金属材料', label: '非金属材料类'},
            {value: '-建筑', label: '建筑类'},
          ]
        },
        {
          value: '土木', label: '土木建筑',
          children: [
            {value: '-建筑设计', label: '建筑设计类'},
            {value: '-城乡', label: '城乡规划与管理类'},
            {value: '-土建施工', label: '土建施工类'},
            {value: '-建筑设备', label: '建筑设备类'},
            {value: '-建筑', label: '建筑工程管理类'},
            {value: '-市政', label: '市政类'},
            {value: '-房地产', label: '房地产类'},
          ]
        },
        {
          value: '水利', label: '水力',
          children: [
            {value: '-水文水资源', label: '水文水资源类'},
            {value: '-水利工程', label: '水利工程与管理类'},
            {value: '-水力水电设备', label: '水力水电设备类'},
            {value: '-水土保持', label: '水土保持与水环境类'},
          ]
        },
        {
          value: '装备', label: '装备制造',
          children: [
            {value: '-机械设计制造', label: '机械设计制造类'},
            {value: '-机电设备', label: '机电设备类'},
            {value: '-自动化', label: '自动化类'},
            {value: '-铁道装备', label: '铁道装备类'},
            {value: '-船舶与海洋工程装备', label: '装备与海洋工程装备类'},
            {value: '-航空装备', label: '航空装备类'},
            {value: '-汽车制造', label: '汽车制造类'},
          ]
        },
        {
          value: '生物', label: '生物与化工',
          children: [
            {value: '-生物技术', label: '生物技术类'},
            {value: '-化工技术', label: '化工技术类'},
          ]
        },
        {
          value: '轻工', label: '轻工纺织',
          children: [
            {value: '-轻化工', label: '轻化工类'},
            {value: '-包装', label: '包装类'},
            {value: '-印刷', label: '印刷类'},
            {value: '-纺织服装', label: '纺织服装类'},
          ]
        },
        {
          value: '食品药品', label: '食品药品与粮食',
          children: [
            {value: '-食品工业', label: '食品工业类'},
            {value: '-药品制造', label: '药品制造类'},
            {value: '-食品药品', label: '食品药品类'},
            {value: '-粮食工业', label: '粮食工业类'},
            {value: '-粮食储检', label: '粮食储检类'},
          ]
        },
        {
          value: '交通', label: '交通运输',
          children: [
            {value: '-铁道运输', label: '铁道运输类'},
            {value: '-道路运输', label: '道路运输类'},
            {value: '-水上运输', label: '水上运输类'},
            {value: '-航空运输', label: '航空运输类'},
            {value: '-管道运输', label: '管道运输类'},
            {value: '-城市轨道交通', label: '城市轨道交通类'},
            {value: '-邮政', label: '邮政类'},
          ]
        },
        {
          value: '电子', label: '电子信息',
          children: [
            {value: '-电子信息', label: '电子信息类'},
            {value: '-计算机', label: '计算机类'},
            {value: '-通信', label: '通信类'},
          ]
        },
        {
          value: '医药', label: '医药卫生',
          children: [
            {value: '-临床', label: '临床类'},
            {value: '-护理', label: '护理类'},
            {value: '-药学', label: '药学类'},
            {value: '-医药技术', label: '医药技术类'},
            {value: '-康复治疗', label: '康复治疗类'},
            {value: '-公共卫生与卫生管理', label: '公共卫生与卫生管理类'},
            {value: '-人口与计划生育', label: '人口与计划生育类'},
            {value: '-健康管理与促进', label: '健康管理与促进类'},
          ]
        },
        {
          value: '财经', label: '财经商贸',
          children: [
            {value: '-财政税务', label: '财政税务类'},
            {value: '-金融', label: '金融类'},
            {value: '-财务会计', label: '财务会计类'},
            {value: '-统计', label: '统计类'},
            {value: '-经济贸易', label: '经济贸易类'},
            {value: '-工商管理', label: '工商管理类'},
            {value: '-市场营销', label: '市场营销类'},
            {value: '-电子商务', label: '电子商务类'},
            {value: '-物流', label: '物流类'},
          ]
        },
        {
          value: '旅游', label: '旅游',
          children: [
            {value: '-旅游', label: '旅游类'},
            {value: '-餐饮', label: '餐饮类'},
            {value: '-会展', label: '会产类'},
          ]
        },
        {
          value: '文化', label: '文化艺术',
          children: [
            {value: '-艺术设计', label: '艺术设计类'},
            {value: '-表演艺术', label: '表演艺术类'},
            {value: '-民族文化', label: '民族文化类'},
            {value: '-文化服务', label: '文化服务类'},
          ]
        },
        {
          value: '新闻', label: '新闻传播',
          children: [
            {value: '-新闻出版', label: '新闻出版类'},
            {value: '-广播', label: '广播类'},
          ]
        },
        {
          value: '教育', label: '教育与体育',
          children: [
            {value: '-教育', label: '教育类'},
            {value: '-语言', label: '语言类'},
            {value: '-文秘', label: '文秘类'},
            {value: '-体育', label: '体育类'},
          ]
        },
        {
          value: '公安', label: '公安与司法',
          children: [
            {value: '-公安管理', label: '公安管理类'},
            {value: '-公安指挥', label: '公安指挥类'},
            {value: '-公安技术', label: '公安技术类'},
            {value: '-侦查', label: '侦查类'},
            {value: '-法律实务', label: '法律实务类'},
            {value: '-法律执行', label: '法律执行类'},
            {value: '-司法', label: '司法类'},
          ]
        },
        {
          value: '公共管理', label: '公共管理与服务',
          children: [
            {value: '-公共事业', label: '公共事业类'},
            {value: '-公共管理', label: '公共管理类'},
            {value: '-公共服务', label: '公共服务类'},
          ]
        },
      ],
      // 类型
      options4: [
        {
          value: '大学特色', label: '大学特色',
          children: [
            {value: '-985', label: '985'},
            {value: '-211', label: '211'},
            {value: '-一流大学', label: '一流大学'},
            {value: '-一流学科', label: '一流学科'},
            {value: '-硕士', label: '硕士点'},
            {value: '-博士', label: '博士点'},
            {value: '-强基', label: '强基计划'},
          ]
        },
        {
          value: '办学性质', label: '办学性质',
          children: [
            {value: '-民办', label: '民办'},
            {value: '-公办', label: '公办'},
            {value: '-中外合作', label: '中外合作办学'},
          ]
        },
        {
          value: '大学类型', label: '大学类型',
          children: [
            {value: '-综合', label: '综合'},
            {value: '-理工', label: '理工'},
            {value: '-财经', label: '财经'},
            {value: '-医学', label: '医学'},
            {value: '-语言', label: '语言'},
            {value: '-农业', label: '农业'},
            {value: '-林业', label: '林业'},
            {value: '-师范', label: '师范'},
            {value: '-体育', label: '体育'},
            {value: '-政法', label: '政法'},
            {value: '-艺术', label: '艺术'},
            {value: '-民族', label: '民族'},
            {value: '-军事', label: '军事'},
          ]
        },
      ],
    }
  },
  methods:{
    // 获得cookies
    getCookies(){
      this.user_name = this.$cookies.get('user_name');
    },

    Major_show(val){
      if(val == '本科'){
        return 1;
      }else if(val == '专科'){
        return 2;
      }else {
        return false;
      }
    },

    // 记得解开！！！！

    // 传递数据
    // giveData(){
    //   if(this.radio == ''){
    //     this.$message.warning('请选择填报批次！');
    //   }else {
    //     const loading = this.$loading({
    //       lock:true,
    //       text:'',
    //       spinner:'',
    //       background:'rgba(0, 0, 0, 0.7)',
    //     });
    //
    //     var num = 0;
    //     var arr;
    //
    //     if(this.button_flag == true){
    //       num = 1;
    //     }
    //     else {
    //       num = 0;
    //     }
    //
    //     if(this.radio == '本科'){
    //       arr = this.mod_major_ben;
    //     }else {
    //       arr = this.mod_major_zhuan;
    //     }
    //
    //     this.axios({
    //       method:'get',
    //       url:'http://101.34.248.53:8181/Map/Voluntary/Voluntary_Intelligent/' + this.user_name + '/' + this.radio + '/'
    //           + this.mod_add + '/' + arr + '/' + this.mod_sch_style + '/' + num
    //     }).then((resp)=>{
    //       console.log(resp.data)
    //       if(resp.data == 'QVAN' || resp.data == 'OK'){
    //         loading.close();
    //         this.$message.success('生成成功！');
    //       }else if(resp.data == "QUAN") {
    //         loading.close();
    //         this.$message.success('生成成功！');
    //       }
    //       else{
    //         loading.close();
    //         this.$message.warning('生成成功！');
    //       }
    //     });
    //   }
    // },

    // 获取用户分数
    getMark(){
      this.axios('http://101.34.248.53:8181/Map/Voluntary/Voluntary_Info_if/' + this.user_name,{
        method:'get'
      }).then((resp)=>{
        this.mark = resp.data.Mark;

        if(this.mark >= 444){
          this.radio = '本科';
        }
        else {
          this.radio = '专科';
        }
      })
    },

    // 是否灰掉本科专业
    disMajor(val){
      if(val < 444){
        return true;
      }else {
        return false;
      }
    }
  },
  created() {
    this.getCookies();
    this.getMark();
  }
}
</script>

<style scoped>
#card{
  width: 30vw;
  height: 105vh;
  /*border: 1px solid blue;*/
  text-align: center;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.4);
  margin: 0 auto;
  padding: 10px;
}

#plan-box{
  margin-top: 20px;
}

#switch-box{
  margin-top: 20px;
}

.switch-tit{
  margin: 0 10px;
}
</style>