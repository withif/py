import unittest
from unittest import TestCase

from test6 import air_conditioner, human, student, car, notebook, monkey

# 单元测试
class myTest(unittest.TestCase):
    def test_air_c(self):
        a=air_conditioner()
        a.setBrand("小米")
        a.setPrice(1000)
        print("空调品牌：",a.getBrand())
        print("空调价格",a.getPrice())
        a.start()
        a.over(10)
    def test_human(self):
        a=human("奥特曼","male",18,100,"小米",0.7,6.3,18,1000)
        a.call(10,15543728796)

    def test_student(self):
        a=student(1001,"lisi",19,"male",187,140,89,"北京市",12345678910)
        a.study(10)
        a.playgame("原神")
        a.programming(1000)
        print(a.sum(1,2,3,4,5,6,7,8,9,10))

    # 创建：法拉利，宝马，铃木，五菱，拖拉机对象
    def test_car(self):
        car1=car("法拉利",4,"red",30,20)
        car2 = car("宝马", 4, "red", 30, 20)
        car3 = car("铃木", 4, "red", 30, 20)
        car4 = car("五菱", 4, "red", 30, 20)
        car5 = car("拖拉机", 4, "red", 30, 20)
        car1.run(car.off_road(car1))
        car2.run(car.off_road(car2))
        car3.run(car.off_road(car3))
        car4.run(car.off_road(car4))
        car5.run(car.off_road(car5))


    def test_notebook(self):
        a=notebook("戴尔",2,"red",4,"i7-12900","4G","512G")
        a.office()
        a.play_games("英雄联盟")



    def test_monkey(self):
        m=monkey("孙悟空","雄性","black",50)
        m.makefire("木材")
        m.study("语文","数学","英语")

if __name__ == '__main__':
    unittest.main()


































