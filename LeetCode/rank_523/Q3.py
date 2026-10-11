class BusBooking:

    def __init__(self, n: int):
        self.rows = n  # 有n排  窗A B | C D窗
        self.seats_list = {} # 座位表-消耗时间
        self.total_time = 0
        self.cnt_seq = 0
        self.sequence = set()

    def toggle(self, seat: str) -> None:
        # seat like C7,D7
        
        if seat in self.sequence:  #该位置已经存在，进行移除
            self.sequence.remove(seat)  #判断是否已经存在序列中移除
            if self.seats_list[seat] == 3:
                self.cnt_seq -= 1  #从优化计数中移除 
            self.total_time -= self.seats_list[seat] #减去时间
            self.seats_list.pop(seat,None)  #从字典中移除
           
        else:  # 添加新位置，判断是否需要+2s时间开销
            partner_prefix = {'A':'B','D':'C'}.get(seat[0])
            if partner_prefix and partner_prefix + seat[1:] in self.sequence:
                self.seats_list[seat] = 3
                self.cnt_seq += 1
            else:
                self.seats_list[seat] = 1
            # if seat[0] == 'A':
            #     B_seat = 'B'+seat[1:]
            #     if B_seat in self.sequence:
            #         self.seats_list[seat] = 3
            #         self.cnt_seq += 1              #说明其可以被优化
            #     else:
            #         self.seats_list[seat] = 1
                
            # elif seat[0] == 'D':
            #     C_seat = 'C'+seat[1:]
            #     if C_seat in self.sequence:
            #         self.seats_list[seat] = 3
            #         self.cnt_seq += 1 
            #     else:
            #         self.seats_list[seat] = 1
            # else: # 是B,C座位，正常添加
            #     self.seats_list[seat] = 1

            self.sequence.add(seat) #更新序列表
            self.total_time += self.seats_list[seat]  #更新总共时间

    def getTotalTime(self) -> int:
        return self.total_time
    
    def getMinTime(self) -> int:    
        Min_time = self.total_time - 2 * self.cnt_seq
        return Min_time


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()

#test1
# obj = BusBooking(10)
# obj.toggle('C7')
# obj.toggle('D7')
# print(f"seat = {obj.seats_list}")
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()
# print(param_2,param_3)

#test2
obj = BusBooking(12)
obj.toggle('D5')
obj.toggle('B2')
param_2 = obj.getTotalTime()
obj.toggle('C1')
obj.toggle('D10')
param_3 = obj.getMinTime()
param_4 = obj.getTotalTime()
print(param_2,param_3,param_4)
print(obj.seats_list)
