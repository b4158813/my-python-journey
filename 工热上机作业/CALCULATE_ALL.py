
class Solution(object):

    def calculate_1(self, h1, h2, h2_):  # 忽略泵功
        self.ans = (h1 - h2) / (h1 - h2_)  # 计算朗肯循环热效率
        self.nt = '{:.2f}'.format(self  .ans * 100) + '%'  # 格式化一下
        return self.nt

    # print(calculate_1(3331.2,2136.8,151.95))

    def calculate_2(self, h1, h2, h2_1, ha, hb, h2_2, h2_lang):  # 忽略泵功
        self.nt = (h1 - hb + ha - h2) / (h1 - h2_1 + ha - hb)  # 计算再热循环热效率
        self.nt_lang = (h1 - h2_lang) / (h1 - h2_1)  # 计算朗肯循环热效率
        self.x2 = (h2 - h2_1) / (h2_2 - h2_1)  # 计算2点干度
        self.nt_format = '{:.2f}'.format(self.nt * 100) + '%'  # 格式化一下
        self.nt_lang_format = '{:.2f}'.format(self.nt_lang * 100) + '%'  # 格式化一下
        self.nt_real = '{:.2f}'.format(0.85 * self.nt * 100) + '%'  # 计算实际值 并格式化一下
        return self.nt_lang_format, self.nt_format, self.x2, self.nt_real

    # print(calculate_2(3349.6, 2183.6, 151.95, 3344.6, 2965.5, 2566.2, 1998.0))#a1点
    # print(calculate_2(3349.6, 2421.7, 151.95, 3376.0, 2639.9, 2566.2, 1998.0))#a2点

    # nt_lang, nt, x2, nt_real = calculate_2(3349.6, 2183.6, 151.95, 3344.6, 2965.5, 2566.2, 1998.0)#测试一下，序列解包
    # print(calculate_2(3349.6, 2183.6, 151.95, 3344.6, 2965.5, 2566.2, 1998.0))# a1点

    def calculate_3(self, h1, h2, h2_1, ha, ha_1):
        self.alpha = (ha_1 - h2_1) / (ha - h2_1)  # alpha计算
        self.nt = (h1 - ha + (1 - self.alpha) * (ha - h2)) / (h1 - ha_1)  # 热效率
        self.nt_lang = (h1 - h2) / (h1 - h2_1)  # 朗肯 热效率
        self.d_lang = 1 / (h1 - h2)  # 朗肯 耗汽率
        # self.d = self.alpha  # 耗汽率
        self.d = 1 / (h1 - ha + (1 - self.alpha) * (ha - h2))
        self.nt_format = '{:.2f}'.format(self.nt * 100) + '%'  # 格式化一下
        self.nt_lang_format = '{:.2f}'.format(self.nt_lang * 100) + '%'  # 格式化一下
        self.d_format = '{:.6f}'.format(self.d) + 'kWh'  # 格式化一下
        self.d_lang_format = '{:.6f}'.format(self.d_lang) + 'kWh'  # 格式化一下
        self.nt_real_format = '{:.2f}'.format(0.85 * self.nt * 100) + '%'  # 格式化一下
        return self.nt_format, self.d_format, self.nt_lang_format, self.d_lang_format,self.nt_real_format  # （nt，d，朗肯nt，朗肯d，真实nt）


# solution = Solution()
# ans = solution.calculate_1(3331.2,2136.8,151.95)
# print(ans)
# ans = solution.calculate_3(3317.5,2100,152,2748.6,640)
# print(ans)
