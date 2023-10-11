using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bai10
{
    class khachThanThiet:HoaDon,IVip
    {
        public khachThanThiet(string maK, string tenK, string ngay, Xang a, int so)
            : base(maK, tenK, ngay, a, so)
        { }
        public override double khuyenMai()
        {
            if (soLuong > 60)
                return 0.04 * soLuong;
            else if (thanhTien() >= 800 && soLuong <= 50)
                return 0.03 * thanhTien();
            return 0;
        }
        public double tamUng()
        {
            return 0.6 * tongThanhTien();
        }
        public double laiSuat()
        {
            return 0.03 * (tongThanhTien() - tamUng());
        }
        public override void xuatTT()
        {
            base.xuatTT();
            Console.Write("{0}\t{1}", tamUng(), laiSuat());
        }

    }
}
