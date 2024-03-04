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
yuan_1 = []
yuan_2 = []
yuan_3 = []
yuan_4 = []
yuan_5 = []
yuan_6 = []
yuan_7 = []
yuan_8 = []
yuan_9 = []
yuan_10 = []
yuan_11 = []
yuan_12 = []
yuan_13 = []
yuan_14 = []
yuan_15 = []
yuan_16 = []
yuan_17 = []
yuan_18 = []
yuan_19 = []
yuan_20 = []
yuan_21 = []
yuan_22 = []
yuan_23 = []
yuan_24 = []
yuan_25 = []
yuan_26 = []
yuan_27 = []
yuan_28 = []
yuan_29 = []
yuan_30 = []
yuan_31 = []
yuan_32 = []
yuan_33 = []
yuan_34 = []
yuan_35 = []
yuan_36 = []
yuan_37 = []
yuan_38 = []
yuan_39= []
yuan_40 = []
yuan_41 = []
yuan_42 = []
yuan_43 = []
yuan_44 = []
yuan_45 = []
yuan_46 = []
yuan_47 = []
yuan_48 = []
yuan_49 = []
yuan_50 = []
yuan_51 = []
yuan_52 = []
yuan_53 = []
yuan_54 = []
yuan_55 = []
yuan_56 = []
yuan_57 = []
yuan_58= []
yuan_59 = []
yuan_60 = []
yuan_61 = []
yuan_62 = []

'''
https://raw.githubusercontent.com/Sgzhlh/JBull/master/Football/Popular Club/AC Milan/AC Milan F.C Ronaldinho 2009_2010 Home Retro Premium Jersey/01.jpg
'''
#source_dir_name = r'D:\python_code\AC Milan'
source_dir_name = input(r'请输入完整路径:')
sku_name_pre = 'jbull-0'



image_pre = "https://raw.githubusercontent.com/Sgzhlh/JBull/master/Football/Popular Club/AC Milan/"
description_str = '<p class="p1">—Retro Jersey SIZE CHART (cm)</p>\n<p class="p1"><span class="Apple-converted-space">      </span>S: <span class="Apple-converted-space">    </span>Chest - 100 cm <span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 69 cm</p>\n<p class="p1"><span class="Apple-converted-space">      </span>M:<span class="Apple-converted-space">    </span>Chest<span class="Apple-converted-space">  </span>- 105 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 73 cm</p>\n<p class="p1"><span class="Apple-converted-space">      </span>L:<span class="Apple-converted-space">      </span>Chest<span class="Apple-converted-space">  </span>- 110 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 76 cm</p>\n<p class="p1"><span class="Apple-converted-space">      </span>XL:<span class="Apple-converted-space">    </span>Chest<span class="Apple-converted-space">  </span>- 115 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 79 cm</p>\n<p class="p1"><span class="Apple-converted-space">       </span>XXL:<span class="Apple-converted-space">  </span>Chest<span class="Apple-converted-space">  </span>- 120 cm<span class="Apple-converted-space">  </span>, <span class="Apple-converted-space">  </span>Length - 82 cm</p>\n<p class="p1"><span class="Apple-converted-space"> </span>—SHIPPING AND HANDLING</p>\n<p class="p1"><span class="Apple-converted-space">       </span>Free Shipping 2-5 business days (Depending on your Region)</p>\n<p class="p1"><span class="Apple-converted-space">       </span>Each customer has a 24 hour handling time period after their purchase in which they can cancel, edit, change, or replace any order.</p>\n<p class="p1"><span class="Apple-converted-space">       </span>After 3-4 business days you will receive an email confirming your order was shipped, and a tracking number you can use to track your order on our Track Your Order page</p>\n<p class="p1"><span class="Apple-converted-space"> </span>—REFUNDS AND RETURNS</p>\n<p class="p1"><span class="Apple-converted-space">         </span>If you are not 100% satisficed with your order all jerseys can be returned and refunded within 14 days after receiving your order.</p>\n<p class="p1"><span class="Apple-converted-space">         </span>Jerseys must be returned with tags attached</p>\n<p class="p1"><span class="Apple-converted-space">         </span>Buyer must pay return shipping unless we have made a mistake on your order</p>\n<p class="p1"><span class="Apple-converted-space">         </span>Visit our Return/Refund Policy page for more information</p>'
shuxing_value_list = ['S', 'M', 'L', 'XL', '2XL']

def getUniqueId():
    start_num = 100000
    end_num = 999999
    return random.randint(start_num,end_num)

def validPrice(dir_name):
    # 判断str 是否有Long
    long_tip = 'Long'
    if re.search(long_tip, dir_name):
        cuxiao_price = 44.99
        normal_price = 94.99
    else:
        cuxiao_price = 39.99
        normal_price = 89.99
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
    img_url = ','.join(img_url)

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
    yuan_1.append('')
    yuan_2.append('')
    yuan_3.append('')
    yuan_4.append('default')
    yuan_5.append('')
    yuan_6.append('838')
    yuan_7.append('')
    yuan_8.append('none')
    yuan_9.append('inherit')
    yuan_10.append('inherit')
    yuan_11.append('inherit')
    yuan_12.append('after')
    yuan_13.append('')
    yuan_14.append('')
    yuan_15.append('')
    yuan_16.append('')
    yuan_17.append('')
    yuan_18.append('')
    yuan_19.append('')
    yuan_20.append('')
    yuan_21.append('')
    yuan_22.append('')
    yuan_23.append('')
    yuan_24.append('')
    yuan_25.append('')
    yuan_26.append('')
    yuan_27.append('')
    yuan_28.append('')
    yuan_29.append('')
    yuan_30.append('')
    yuan_31.append('')
    yuan_32.append('')
    yuan_33.append('')
    yuan_34.append('')
    yuan_35.append('S')
    yuan_36.append('classic-editor')
    yuan_37.append('25')
    yuan_38.append('')
    yuan_39.append('')
    yuan_40.append('bottom')
    yuan_41.append('')
    yuan_42.append(1)
    yuan_43.append('default')
    yuan_44.append('default')
    yuan_45.append('none')
    yuan_46.append('')
    yuan_47.append('')
    yuan_48.append('')
    yuan_49.append('')
    yuan_50.append('')
    yuan_51.append('')
    yuan_52.append('')
    yuan_53.append('')
    yuan_54.append('text')
    yuan_55.append('')
    yuan_56.append('')
    yuan_57.append('')
    yuan_58.append('text')
    yuan_59.append('')
    yuan_60.append('')
    yuan_61.append(0)
    yuan_62.append('')


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
        yuan_1.append('')
        yuan_2.append('')
        yuan_3.append('')
        yuan_4.append('')
        yuan_5.append('')
        yuan_6.append('')
        yuan_7.append('')
        yuan_8.append('')
        yuan_9.append('')
        yuan_10.append('')
        yuan_11.append('')
        yuan_12.append('')
        yuan_13.append('')
        yuan_14.append('')
        yuan_15.append('')
        yuan_16.append('')
        yuan_17.append('')
        yuan_18.append('')
        yuan_19.append('')
        yuan_20.append('')
        yuan_21.append('')
        yuan_22.append('')
        yuan_23.append('')
        yuan_24.append('')
        yuan_25.append('')
        yuan_26.append('')
        yuan_27.append('')
        yuan_28.append('')
        yuan_29.append('')
        yuan_30.append('')
        yuan_31.append('')
        yuan_32.append('')
        yuan_33.append('')
        yuan_34.append('')
        yuan_35.append('')
        yuan_36.append('')
        yuan_37.append('')
        yuan_38.append('')
        yuan_39.append('')
        yuan_40.append('')
        yuan_41.append('')
        yuan_42.append('')
        yuan_43.append('')
        yuan_44.append('')
        yuan_45.append('')
        yuan_46.append('')
        yuan_47.append('')
        yuan_48.append('')
        yuan_49.append('')
        yuan_50.append('')
        yuan_51.append('')
        yuan_52.append('')
        yuan_53.append('')
        yuan_54.append('')
        yuan_55.append('')
        yuan_56.append('')
        yuan_57.append('')
        yuan_58.append('')
        yuan_59.append('')
        yuan_60.append('')
        yuan_61.append('')
        yuan_62.append('')


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

    '元数据：_elementor_edit_mode':yuan_1,
    '元数据：_elementor_template_type':yuan_2,
    '元数据：_elementor_version':yuan_3,
    '元数据：_wp_page_template':yuan_4,
    '元数据：_elementor_data':yuan_5,
    '元数据：woodmart_sguide_select'	:yuan_6,
    '元数据：_product_360_image_gallery'	:yuan_7,
    '元数据：_woodmart_whb_header':yuan_8,
    '元数据：_woodmart_product_design':yuan_9,
    '元数据：_woodmart_single_product_style'	:yuan_10,
    '元数据：_woodmart_thums_position':yuan_11,
    '元数据：_woodmart_extra_position':yuan_12,
    '属性 2 名称':yuan_13,
    '属性 2 值'	:yuan_14,
    '属性 2 可见	':yuan_15,
    '属性 2  的全局'	:yuan_16,
    '属性 3 名称	':yuan_17,
    '属性 3 值'	:yuan_18,
    '属性 3 可见	':yuan_19,
    '属性 3  的全局'	:yuan_20,
    '属性 4 名称	':yuan_21,
    '属性 4 值'	:yuan_22,
    '属性 4 可见	':yuan_23,
    '属性 4  的全局'	:yuan_24,
    '属性 5 名称'	:yuan_25,
    '属性 5 值':yuan_26,
    '属性 5 可见	':yuan_27,
    '属性 5  的全局'	:yuan_28,
    '元数据：_woodmart_product_video	:yuan_1':yuan_29,
    '元数据：_oembed_992c44b3a32aec363189635e67914edf':yuan_30,
    '元数据：_oembed_time_992c44b3a32aec363189635e67914edf'	:yuan_31,
    '元数据：_oembed_db09be560b4aefcb5b04e498f87b8563'	:yuan_32,
    '元数据：_woodmart_new_label	':yuan_33,
    '元数据：_woodmart_extra_content	':yuan_34,
    '属性 1  的默认值':yuan_35,
    '元数据：_last_editor_used_jetpack'	:yuan_36,
    '元数据：rank_math_seo_score':yuan_37,
    '元数据：woodmart_price_unit_of_measure'	:yuan_38,
    '元数据：_rank_math_gtin_code':yuan_39,
    '元数据：_ppcp_button_position':yuan_40,
    '元数据：woodmart_total_stock_quantity':yuan_41,
    '元数据：rank_math_internal_links_processed':yuan_42,
    '元数据：_woodmart_main_layout':yuan_43,
    '元数据：_woodmart_sidebar_width	':yuan_44,
    '元数据：_woodmart_custom_sidebar':yuan_45,
    '元数据：_woodmart_new_label_date':yuan_46,
    '元数据：_woodmart_swatches_attribute':yuan_47,
    '元数据：_woodmart_related_off':yuan_48,
    '元数据：_woodmart_exclude_show_single_variation	':yuan_49,
    '元数据：_woodmart_product_hashtag':yuan_50,
    '元数据：_woodmart_product-background':yuan_51,
    '元数据：_woodmart_hide_tabs_titles'	:yuan_52,
    '元数据：_woodmart_product_custom_tab_title'	:yuan_53,
    '元数据：_woodmart_product_custom_tab_content_type':yuan_54,
    '元数据：_woodmart_product_custom_tab_content':yuan_55,
    '元数据：_woodmart_product_custom_tab_html_block	':yuan_56,
    '元数据：_woodmart_product_custom_tab_title_2':yuan_57,
    '元数据：_woodmart_product_custom_tab_content_type_2':yuan_58,
    '元数据：_woodmart_product_custom_tab_content_2'	:yuan_59,
    '元数据：_woodmart_product_custom_tab_html_block_2':yuan_60,
    '元数据：rank_math_primary_product_cat':yuan_61,
    '元数据：wd_additional_variation_images_data':yuan_62

}
)
#house.columns['ID','类型','SKU','名称','已发布','是推荐产品','在列表页可见','简单描述','描述','促销开始日期','促销截止日期','税状态','税类','有货？','库存','库存不足','允许缺货下单？','单独出售','重量(公斤)','长度(厘米)','宽度（厘米）','高度（厘米）','允许客户评价？','购物备注','促销价格','常规售价','分类','标签','运费类','图片','下载限制','下载的过期天数','父级','分组产品','交叉销售','交叉销售','外部链接','按钮文本','位置','属性 1 名称','属性 1 值','属性 1 可见','属性 1  的全局']
#查看数据表的内容

#读csv时去掉序号列
# house.drop([0],axis=1,inplace=True)
# print(house)

house.head()
#导出csv时去掉序号列
house.to_csv(source_dir_name+'/wc.csv',index=False,encoding='utf-8')

















