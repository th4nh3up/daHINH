using System;
namespace dahinh
{
	public class hangHoa
    {
        string maHang;
        public string tenHang;
        public int checkSoMaHang(string m)
        {
            int num;
            if (m.Length == 5 && m.EndsWith(m.Substring(m.Length - 3)) && (int.TryParse(m.Substring(m.Length - 3), out num)))
                return num;
            return 0;
        }
        public string ma
        {
            get { return maHang; }
            set
            {
                if (!value.StartsWith("HH") && value.Length != 6 && checkSoMaHang(value) == 0)
                    maHang = "HH001";
                else
                    maHang = value;
            }
        }
        public hangHoa()
        {
            ma = tenHang = "";
        }
        public hangHoa(string a, string b)
        {
            ma = a;
            tenHang = b;
        }
        public virtual void nhap()
        {
            Console.WriteLine("Nhap ma hang: ");
            ma = Console.ReadLine();
            Console.WriteLine("Nhap ten hang: ");
            tenHang = Console.ReadLine();
        }
        public virtual void xuat()
        {
            Console.WriteLine("Ma: {0}\tTen: {1}", ma, tenHang);
        }
    }
}

