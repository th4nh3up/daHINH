using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bai10
{
    class Program
    {
        static void Main(string[] args)
        {
            danhSachHoaDon a = new danhSachHoaDon();
            a.docFile("../../hoaDon.xml");
            a.xuatDS();
            Console.ReadLine();
        }
    }
}
