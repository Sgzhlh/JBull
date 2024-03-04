# -*- coding: utf-8 -*-
"""
@Time    :  
@Author  : wu junfeng
@File    : .py

"""
import requests
import os
import re
import pandas as pd
import random

ID = []
string_type = []
sku = []
name = []
is_publish = []
is_popular = []
is_visible = []
description = []
brief_description = []
cuxiao_start_time = []
cuxiao_deadline_time = []
sui_status = []
sui_type = []
is_youhuo = []
kucun = []
kucun_buzu = []
quehuo_xiadan = []
single_sale = []
weight = []
changdu = []
kuandu = []
gaodu =[]
kehupingjia = []
gouwubeizhu  = []
cuxiao_price = []
changgui_price = []
fenlei = []
biaoqian = []
yunfeilei = []
tupian_url = []
xiazzai_limit = []
xiazai_expire_days = []
fuji = []
fenzhu_product = []
jiaocha_sale = []
outside_url = []
buttion_text = []
weizhi = []
shuxing_name = []
shuxing_value = []
shuxing_visible = []
shuxing_global = []

'''
https://raw.githubusercontent.com/Sgzhlh/JBull/master/Football/Popular Club/AC Milan/AC Milan F.C Ronaldinho 2009_2010 Home Retro Premium Jersey/01.jpg
'''
#source_dir_name = r'D:\python_code\AC Milan'
source_dir_name = input(r'请输入AC Milan的完整路径(类似D:\python_code\AC Milan):')
sku_name_pre = 'jbull-0'



image_pre = "https://raw.githubusercontent.com/Sgzhlh/JBull/master/Football/Popular Club/AC Milan/"
description_str = '<p class="p1">—Retro Jersey SIZE CHART (cm)</p>\n<p class="p1"><span class="Apple-converted-space">      </span>S: <span class="Apple-converted-space">    </span>Chest - 100 cm <span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 69 cm</p>\n<p class="p1"><span class="Apple-converted-space">      </span>M:<span class="Apple-converted-space">    </span>Chest<span class="Apple-converted-space">  </span>- 105 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 73 cm</p>\n<p class="p1"><span class="Apple-converted-space">      </span>L:<span class="Apple-converted-space">      </span>Chest<span class="Apple-converted-space">  </span>- 110 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 76 cm</p>\n<p class="p1"><span class="Apple-converted-space">      </span>XL:<span class="Apple-converted-space">    </span>Chest<span class="Apple-converted-space">  </span>- 115 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 79 cm</p>\n<p class="p1"><span class="Apple-converted-space">       </span>XXL:<span class="Apple-converted-space">  </span>Chest<span class="Apple-converted-space">  </span>- 120 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 82 cm</p>\n<p class="p1"><span class="Apple-converted-space"> </span>—SHIPPING AND HANDLING</p>\n<p class="p1"><span class="Apple-converted-space">       </span>Free Shipping 2-5 business days (Depending on your Region)</p>\n<p class="p1"><span class="Apple-converted-space">       </span>Each customer has a 24 hour handling time period after their purchase in which they can cancel, edit, change, or replace any order.</p>\n<p class="p1"><span class="Apple-converted-space">       </span>After 3-4 business days you will receive an email confirming your order was shipped, and a tracking number you can use to track your order on our Track Your Order page</p>\n<p class="p1"><span class="Apple-converted-space"> </span>—REFUNDS AND RETURNS</p>\n<p class="p1"><span class="Apple-converted-space">         </span>If you are not 100% satisficed with your order all jerseys can be returned and refunded within 14 days after receiving your order.</p>\n<p class="p1"><span class="Apple-converted-space">         </span>Jerseys must be returned with tags attached</p>\n<p class="p1"><span class="Apple-converted-space">         </span>Buyer must pay return shipping unless we have made a mistake on your order</p>\n<p class="p1"><span class="Apple-converted-space">         </span>Visit our Return/Refund Policy page for more information</p>'
shuxing_value_list = ['S', 'M', 'L', 'XL', '2XL']

def getUniqueId():
    start_num = 100000
    end_num = 999999
    return random.randint(start_num,end_num)

def validPrice(dir_name):
    # 判断str 是否有long
    long_tip = 'long'
    if re.search(long_tip, dir_name):
        cuxiao_price = 44.99
        normal_price = 94.99
    else:
        cuxiao_price = 44.99
        normal_price = 94.99
    return [cuxiao_price,normal_price]



sku_idx = 0
for single_dir in os.listdir(source_dir_name):

    sku_idx += 1
    image_count = 0

    for file in os.listdir(os.path.join(source_dir_name,single_dir)):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                image_count += 1

    #根据图片数量获取url连接
    img_url = ['https://raw.githubusercontent.com/Sgzhlh/JBull/master/Football/Popular Club/AC Milan/AC Milan F.C Ronaldinho 2009_2010 Home Retro Premium Jersey/0{}.jpg'.format(str(i)) for i in range(1,image_count+1)]
    #转成字符串
    img_url = '，'.join(img_url)

    ID.append(getUniqueId())
    string_type.append('variable')
    sku.append('jbull-0'+str(sku_idx))
    name.append(single_dir)
    is_publish.append(1)
    is_popular.append(0)
    is_visible.append('visible')
    brief_description.append('')
    description.append(description_str)
    cuxiao_start_time.append('')
    cuxiao_deadline_time.append('')
    sui_status.append('taxable')
    sui_type.append('')
    is_youhuo.append(1)
    kucun.append('')
    kucun_buzu.append('')
    quehuo_xiadan.append(0)
    single_sale.append(0)
    weight.append(0.3)
    changdu.append('')
    kuandu.append('')
    gaodu.append('')
    kehupingjia.append(1)
    gouwubeizhu.append('')
    cuxiao_price.append('')
    changgui_price.append('')
    fenlei.append('Accessories')
    biaoqian.append('')
    yunfeilei.append('')
    tupian_url.append(img_url)
    xiazzai_limit.append('')
    xiazai_expire_days.append('')
    fuji.append('')
    fenzhu_product.append('')
    jiaocha_sale.append('')
    outside_url.append('')
    buttion_text.append('')
    weizhi.append(0)
    shuxing_name.append('Size')
    shuxing_value.append('S, M, L, XL, 2XL')
    shuxing_visible.append(1)
    shuxing_global.append(1)


    # #再增加5条数据 S M L XL 2XL
    position = 0
    for i in range(1,6):
        position += 1
        ID.append(getUniqueId())
        string_type.append('variable')
        sku.append('')
        name.append(single_dir)
        is_publish.append(1)
        is_popular.append(0)
        is_visible.append('visible')
        brief_description.append('')
        description.append('')
        cuxiao_start_time.append('')
        cuxiao_deadline_time.append('')
        sui_status.append('taxable')
        sui_type.append('parent')
        is_youhuo.append(1)
        kucun.append('')
        kucun_buzu.append('')
        quehuo_xiadan.append(0)
        single_sale.append(0)
        weight.append('')
        changdu.append('')
        kuandu.append('')
        gaodu.append('')
        kehupingjia.append(0)
        gouwubeizhu.append('')
        cuxiao_price.append(validPrice(single_dir)[0])
        changgui_price.append(validPrice(single_dir)[1])
        fenlei.append('')
        biaoqian.append('')
        yunfeilei.append('')
        tupian_url.append('')
        xiazzai_limit.append('')
        xiazai_expire_days.append('')
        fuji.append(sku_name_pre+str(sku_idx))
        fenzhu_product.append('')
        jiaocha_sale.append('')
        outside_url.append('')
        buttion_text.append('')
        weizhi.append(position)
        shuxing_name.append('Size')
        shuxing_value.append(shuxing_value_list[position - 1])
        shuxing_visible.append('')
        shuxing_global.append(1)



# id_sum   = sum(ID, [])
# string_type_sum = sum(string_type,[])
# sku_sum   = sum(sku,[])
# name_sum   = sum(name,[])
# is_publish_sum = sum(is_publish,[])
# is_popular_sum   = sum(is_popular,[])
# is_visible_sum   = sum(is_visible, [])
# description_sum = sum(description,[])
# brief_description_sum   = sum(brief_description,[])
# cuxiao_start_time_sum   = sum(cuxiao_start_time,[])
# cuxiao_deadline_time_sum = sum(cuxiao_deadline_time,[])
# sui_status_sum   = sum(sui_status,[])
# sui_type_sum   = sum(sui_type,[])
# is_youhuo_sum = sum(is_youhuo,[])
# kucun_sum   = sum(kucun,[])
# kucun_buzu_sum   = sum(kucun_buzu, [])
# quehuo_xiadan_sum = sum(quehuo_xiadan,[])
# single_sale_sum   = sum(single_sale,[])
# weight_sum   = sum(weight, [])
# changdu_sum = sum(changdu,[])
# kuandu_sum   = sum(kuandu,[])
# gaodu_sum   = sum(gaodu, [])
# kehupingjia_sum = sum(kehupingjia,[])
# gouwubeizhu_sum   = sum(gouwubeizhu,[])
# cuxiao_price_sum   = sum(cuxiao_price, [])
# changgui_price_sum = sum(changgui_price,[])
# fenlei_sum   = sum(fenlei,[])
# biaoqian_sum   = sum(biaoqian, [])
# yunfeilei_sum = sum(yunfeilei,[])
# tupian_url_sum   = sum(tupian_url,[])
# xiazzai_limit_sum   = sum(xiazzai_limit, [])
# xiazai_expire_days_sum = sum(xiazai_expire_days,[])
# fuji_sum   = sum(fuji,[])
# fenzhu_product_sum   = sum(fenzhu_product,[])
# jiaocha_sale_sum   = sum(jiaocha_sale,[])
# outside_url_sum   = sum(outside_url,[])
# buttion_text_sum   = sum(buttion_text,[])
# weizhi_sum   = sum(weizhi,[])
# shuxing_name_sum   = sum(shuxing_name,[])
# shuxingxing_value,[])
# shuxing_visible_sum   = sum(shuxing_visible,[])
# shuxing_global_sum = sum(shuxing_global,[])

# 创建数据表
# house = pd.DataFrame({
#     'ID': id_sum,
#     '类型':string_type_sum,
#     'SKU': sku_sum,
#     '名称': name_sum,
#     '已发布': is_publish_sum,
#     '是推荐产品': is_popular_sum,
#     '在列表页可见': is_visible_sum,
#     '简单描述': brief_description_sum,
#     '描述': description_sum,
#     '促销开始日期': cuxiao_start_time_sum,
#     '促销截止日期': cuxiao_deadline_time_sum,
#     '税状态': sui_status_sum,
#     '税类': sui_type_sum,
#     '有货？': is_youhuo_sum,
#     '库存': kucun_sum,
#     '库存不足': kucun_buzu_sum,
#     '允许缺货下单？': quehuo_xiadan_sum,
#     '单独出售': single_sale_sum,
#     '重量(公斤)': weight_sum,
#     '长度(厘米)': changdu_sum,
#     '宽度（厘米）': kuandu_sum,
#     '高度（厘米）': gaodu_sum,
#     '允许客户评价？': kehupingjia_sum,
#     '购物备注': gouwubeizhu_sum,
#     '促销价格': cuxiao_price_sum,
#     '常规售价': changgui_price_sum,
#     '分类': fenlei_sum,
#     '标签': biaoqian_sum,
#     '运费类': yunfeilei_sum,
#     '图片': tupian_url_sum,
#     '下载限制': xiazzai_limit_sum,
#     '下载的过期天数': xiazai_expire_days_sum,
#     '父级': fuji_sum,
#     '分组产品': fenzhu_product_sum,
#     '交叉销售': jiaocha_sale_sum,
#     '交叉销售': jiaocha_sale_sum,
#     '外部链接': outside_url_sum,
#     '按钮文本': buttion_text_sum,
#     '位置': weizhi_sum,
#     '属性 1 名称': shuxing_name_sum,
#     '属性 1 值': shuxing_value_sum,
#     '属性 1 可见': shuxing_visible_sum,
#     '属性 1  的全局': shuxing_global_sum,
# }
# )

# print(
#     ID,string_type,sku,name,is_publish,is_popular,is_visible,brief_description,cuxiao_start_time,cuxiao_deadline_time,sui_status,sui_type,is_youhuo,
# kucun,kucun_buzu,quehuo_xiadan,single_sale,weight,changdu,kuandu,gaodu,kehupingjia,gouwubeizhu,
# cuxiao_price,changgui_price,fenlei,biaoqian,yunfeilei,tupian_url,xiazzai_limit,xiazai_expire_days,
# fuji,fenzhu_product,jiaocha_sale,jiaocha_sale,outside_url,buttion_text,weizhi,shuxing_name,shuxing_value,
# shuxing_visible,shuxing_global
# )
# print(len(ID),len(string_type),len(sku),len(name),len(is_publish),len(is_popular),len(is_visible),len(brief_description),len(cuxiao_start_time),len(cuxiao_deadline_time),len(sui_status),len(sui_type),len(is_youhuo),
#       len(kucun),len(kucun_buzu),len(quehuo_xiadan),len(single_sale),len(weight),len(changdu),len(kuandu),len(gaodu),len(kehupingjia),len(gouwubeizhu),
#       len(cuxiao_price),len(changgui_price),len(fenlei),len(biaoqian),len(yunfeilei),len(tupian_url),len(xiazzai_limit),len(xiazai_expire_days),
#       len(fuji),len(fenzhu_product),len(jiaocha_sale),len(jiaocha_sale),len(outside_url),len(buttion_text),len(weizhi),len(shuxing_name),len(shuxing_value),
#       len(shuxing_visible),len(shuxing_global))

house = pd.DataFrame({
    'ID': ID,
    '类型':string_type,
    'SKU': sku,
    '名称': name,
    '已发布': is_publish,
    '是推荐产品': is_popular,
    '在列表页可见': is_visible,
    '简单描述': brief_description,
    '描述': description,
    '促销开始日期': cuxiao_start_time,
    '促销截止日期': cuxiao_deadline_time,
    '税状态': sui_status,
    '税类': sui_type,
    '有货？': is_youhuo,
    '库存': kucun,
    '库存不足': kucun_buzu,
    '允许缺货下单？': quehuo_xiadan,
    '单独出售': single_sale,
    '重量(公斤)': weight,
    '长度(厘米)': changdu,
    '宽度(厘米)': kuandu,
    '高度(厘米)': gaodu,
    '允许客户评价？': kehupingjia,
    '购物备注': gouwubeizhu,
    '促销价格': cuxiao_price,
    '常规售价': changgui_price,
    '分类': fenlei,
    '标签': biaoqian,
    '运费类': yunfeilei,
    '图片': tupian_url,
    '下载限制': xiazzai_limit,
    '下载的过期天数': xiazai_expire_days,
    '父级': fuji,
    '分组产品': fenzhu_product,
    '交叉销售': jiaocha_sale,
    '交叉销售': jiaocha_sale,
    '外部链接': outside_url,
    '按钮文本': buttion_text,
    '位置': weizhi,
    '属性 1 名称': shuxing_name,
    '属性 1 值': shuxing_value,
    '属性 1 可见': shuxing_visible,
    '属性 1  的全局': shuxing_global,
}
)
#house.columns['ID','类型','SKU','名称','已发布','是推荐产品','在列表页可见','简单描述','描述','促销开始日期','促销截止日期','税状态','税类','有货？','库存','库存不足','允许缺货下单？','单独出售','重量(公斤)','长度(厘米)','宽度（厘米）','高度（厘米）','允许客户评价？','购物备注','促销价格','常规售价','分类','标签','运费类','图片','下载限制','下载的过期天数','父级','分组产品','交叉销售','交叉销售','外部链接','按钮文本','位置','属性 1 名称','属性 1 值','属性 1 可见','属性 1  的全局']
#查看数据表的内容

#读csv时去掉序号列
# house.drop([0],axis=1,inplace=True)
# print(house)

house.head()
#导出csv时去掉序号列
house.to_csv('wc.csv',index=False,encoding='utf-8')

















