class Solution:
    def ordinalOfDate(self, date: str) -> int:
        month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        #分离出年、月、日
        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        #先判断年份是否是闰年
        run_year = self.juggle(year)
        res = 0
        for i in range(1, month):
            res += month_day[i]
        #如果是比2月份大的月份，判断是否超过了2月
        if month > 2:
            #如果是闰年
            if run_year:
                res += 1
        res += day
        return res

    def juggle(self, year:int) -> bool:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif (year % 100) and not (year % 4):
            return True
        else:
            return False