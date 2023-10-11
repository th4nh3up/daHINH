using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bai10
{
    class khachVangLai:HoaDon
    {
        public khachVangLai(string maK, string tenK, string ngay, Xang a, int so)
            : base(maK, tenK, ngay,a , so)
        {

        }
        public override double khuyenMai()
        {
            if (thanhTien() > 1000)
                return 0.03 * thanhTien();
            return 0;
        }
        public override void xuatTT()
        {
            base.xuatTT();
        }
    }
}
