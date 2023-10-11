using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
namespace bai10
{
    class danhSachHoaDon
    {
        List<HoaDon> ds = new List<HoaDon>();
        public void docFile(string tenFile)
        {
            XmlDocument read = new XmlDocument();
            read.Load(tenFile);
            XmlNodeList nodeList = read.SelectNodes("/DSHD/HoaDon");
            foreach(XmlNode node in nodeList)
            {
                HoaDon a;
                int Loai = int.Parse(node["Loai"].InnerText);
                string ma = node["MS"].InnerText;
                string ten = node["Khach"].InnerText;
                string ngay = node["NgayLap"].InnerText;
                XmlNode Hang = node.SelectSingleNode("Hang");
                
                    string maHang = Hang["MH"].InnerText;
                    string tenHang = Hang["TenHang"].InnerText;
                    double gia = double.Parse(Hang["Gia"].InnerText);
                    Xang b = new Xang(maHang, tenHang, gia);
             
                int so = int.Parse(node["Soluong"].InnerText);
                if (Loai == 1)
                {
                    a = new khachVip(ma, ten, ngay, b , so);
                }
                else if (Loai == 2)
                {
                    a = new khachThanThiet(ma, ten, ngay, b, so);
                }
                else
                    a = new khachVangLai(ma, ten, ngay, b , so);
                ds.Add(a);
            }           
        }
        public void xuatDS()
        {
            foreach (HoaDon a in ds)
                a.xuatTT();
        }
       
    }
}
