import unittest
import operaciones as op


class Testop(unittest.TestCase):
    
    def test_upper(self):
        self.assertAlmostEqual(op.sumacplx((9.3,2.5),(-6.5,2)),(2.8000000000000007, 4.5))
        self.assertEqual(op.restcplx((2.5,7),(-1.7,3.4)),(4.2, 3.6))
        self.assertEqual(op.multcplx((3.5,6),(-6.7,2)),(-35.45, -33.2))
        div=op.divcplx((-12,6.5),(-7.2,3.9))
        self.assertAlmostEqual(div[0],1.6666666666666667) 
        self.assertAlmostEqual(div[1], -1.0597207095601793e-16)
        self.assertAlmostEqual(op.modcplx((-10,2)),10.19803902)
        self.assertEqual(op.conjucplx((-7.5,-2)),(-7.5, 2))
        self.assertAlmostEqual(op.fasecplx((-9.5,4.5)),2.6992184306)
        car_a_pol=op.carteapola((-9.4,3.4))
        self.assertAlmostEqual(car_a_pol[0], 9.99599919)
        self.assertAlmostEqual(car_a_pol[1], 2.794531050)
        pol_a_car=op.polacart((9.99599919, 2.79453105))
        self.assertAlmostEqual(pol_a_car[0],-9.4)
        self.assertAlmostEqual(pol_a_car[1], 3.4)
if __name__ == '__main__':
    unittest.main()