using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bai10
{
    abstract class HoaDon
    {
        public string maSo, tenKH, ngayLap;
        Xang matHang;
        public int soLuong;
        public HoaDon(string maK,string tenK, string ngay, Xang a, int so)
        {
            maSo = maK;
            tenKH = tenK;
            ngayLap = ngay;
            matHang = a;
            soLuong = so;
        }
        public virtual double thanhTien()
        {
            return soLuong * matHang.donGia;
        }
        public abstract double khuyenMai();
        public virtual double tongThanhTien()
        {
            return thanhTien() - khuyenMai();
        }
        public virtual void xuatTT()
        {
            Console.WriteLine();
            Console.Write("{0}\t{1}\t{2}\t{3}\t{4}\t", maSo, tenKH, ngayLap, matHang.tenhang, tongThanhTien());
        }

    }
}
