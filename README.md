# taobao-tianmao-auto-buy
淘宝/天猫秒杀抢购

        以下是原作者的说明
        使用步骤：
        1、按格式输入商品链接和开售时间
        2、程序自动打开chrome浏览器访问链接，跳至登陆页面请在30秒内扫码登陆
        3、跳至商品页面请在开售时间前选择所有商品规格（如鞋码、配色）
        4、开售后自动下单，在淘宝规定时间内完成支付
        提示：
        1、必须配合chrome浏览器（71-73版本）使用,只适用于淘宝和天猫
        2、开售时间格式必须正确（xxxx-xx-xx(空格)xx:xx:xx）
        4、扫码登陆后，chrome浏览器可能会拦截重定向请求，如发生请在浏览器地址栏末尾收到跳转网页
        5、跳至商品页面，必须在开售时间前完成 全部 商品规格选择
        6、提前设置默认邮寄地址和电话，中途无法更改
        7、无法在下单页面操作，不适用使用优惠券等情况
        8、程序打包后需要将chromedriver.exe放置在exe同目录下才能运行 
       
        以下是改写说明 2019年11月8日
        1.商品地址、天猫/淘宝、抢购时间 都需要在源代码输入
        2.正式开始时，需要在命令行界面随便说句话
        3.我的运行环境是win7 32bit、Python V3.8、Selenium V3.141、Chrome v73 以及 相应的ChromeDriver，新版应该都没问题，没用到什么奇葩特性。
        4.扫码登录重定向问题 解决不了，建议点网页右上角，手动跳转被屏蔽的页面
        5.Chrome Driver一直提示错误 platform_sensor_reader_win.cc(243) not implemented ，不过不影响使用
        感谢原作者thelastleft-back，感谢Crossin入门课。初学习作，如有不妥之处，请多包涵。
        Have fun.
        
        Change log 2020-01-13
        - Please download corresponding Chrome WebDriver first. Apply to all versions. Download Chrome webdriver https://sites.google.com/a/chromium.org/chromedriver/downloads
        - Copy the chromedriver.exe to your project root folder.
