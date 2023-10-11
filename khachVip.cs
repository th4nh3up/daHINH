using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bai10
{
    class khachVip:HoaDon,IVip
    {
        public khachVip(string maK, string tenK, string ngay, Xang a, int so):base(maK,tenK,ngay,a ,so)
        {

        }
        public override double khuyenMai()
        {
            if (soLuong > 50)
                return 0.05 * soLuong;
            else if (soLuong <= 50 && thanhTien() >= 600)
                return 0.04 * thanhTien();
            else if (soLuong >= 10)
                return 0.01 * thanhTien();
            return 0;
        }
        public override double tongThanhTien()
        {
            return base.tongThanhTien();
        }
        public double tamUng()
        {
            return 0.4 * tongThanhTien();
        }
        public double laiSuat()
        {
            return 0.02 * (tongThanhTien() - tamUng());
        }
        public override void xuatTT()
        {
            base.xuatTT();
            Console.Write("{0}\t{1}", tamUng(), laiSuat());
        }
    }
}
