#图灵机程序
class Controler:
    def __init__(self, raw_state, raw_position, raw_list, program):
        self.state = raw_state
        self.position = raw_position
        self.data_list = raw_list       #存储数据带，'_'表示无数据，数据统一使用str格式
        self.program = program          #索引为元组(str读取所得数据，str控制器状态)，值为程序(str写入数据，str更改状态，int移动)
    def run(self):
        while True:
            if (self.data_list[self.position], self.state) not in self.program.keys():        #检测对应法则是否存在
                print(f'出现错误！({self.data_list[self.position]}, {self.state})未录入程序中!')
                return -1

            if self.program[(self.data_list[self.position], self.state)][2] == 0:           #检测是否成功停机
                if self.data_list[self.position] == self.program[(self.data_list[self.position], self.state)][0] and self.state == self.program[(self.data_list[self.position], self.state)][1]:
                    print('图灵机成功停机！下方为最终数据：')

                    Bool = False
                    output_str = ''
                    for data in self.data_list:
                        if Bool:
                            output_str += ' '
                        else:
                            Bool = True

                        output_str += str(data)
                    print(output_str)

                    return 0

            if self.position == 0 and self.program[(self.data_list[self.position], self.state)][2] ==-1:      #检测是否需要反向延长数据带
                new_list = ['_']
                for data in self.data_list:
                    new_list.append(data)
                self.position += 1
                self.data_list = new_list
            if self.position < 0:           #检测是否需要反向延长多次数据带
                new_list = []
                for i in range(0, -self.position):
                    new_list.append('_')
                for data in self.data_list:
                    new_list.append(data)
                self.position = 0
                self.data_list = new_list
            if self.position == len(self.data_list) - 1 and self.program[(self.data_list[self.position], self.state)][2] == 1:      #检测是否需要正向延长纸袋
                self.data_list.append('_')
            if self.position > len(self.data_list) - 1:           #检测是否需要正向延长多次数据带
                for i in range(0, self.position - len(self.data_list) - 1):
                    self.data_list.append('_')

            temp_data = self.program[(self.data_list[self.position], self.state)][0]
            temp_state = self.program[(self.data_list[self.position], self.state)][1]
            temp_position = self.program[(self.data_list[self.position], self.state)][2]

            self.data_list[self.position] = temp_data
            self.state = temp_state
            self.position += temp_position

raw_state = input('输入初始状态：')
raw_position = int(input('输入初始位置，0表示数据带起点：'))
raw_list = input('输入数据带，_表示空数据，以空格隔开：').split()

# raw_state = 'q1'
# raw_position = 0
# raw_list = ['1', '1', '1', '_', '1', '1', '1']

program = {}
print('下面请依次输入读取所得数据，控制器状态，写入数据，更改状态，移动(用-1，0，1表示)，输入back撤销上一个录入，输入exit退出：')

while True:
    temp_str = input()
    if temp_str == 'back':
        if len(program.keys()) > 0:
            program.pop(program.keys()[-1])
            print('删除成功！')
        else:
            print('删除失败！')
    elif temp_str == 'exit':
        break
    else:
        temp_list = temp_str.split()
        if len(temp_list) == 5:
            program[(temp_list[0], temp_list[1])] = (temp_list[2], temp_list[3], int(temp_list[4]))
        else:
            print('程序非法！')
print('录入结束！')

turing_machine = Controler(raw_state, raw_position, raw_list, program)
turing_machine.run()

"""
1 q1 1 q1 1
_ q1 1 q2 1
1 q2 1 q2 1
_ q2 _ q3 -1
1 q3 _ q3 0
_ q3 _ q3 0
exit
"""