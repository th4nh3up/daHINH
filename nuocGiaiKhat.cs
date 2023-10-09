using System;
namespace dahinh
{
    class nuocGiaiKhat : hangHoa
    {
        string donViTinh;

        public string dvt
        {
            get { return donViTinh; }
            set
            {
                if (value != "Ket" || value != "Thung" || value != "Chai" || value != "Lon")
                    donViTinh = "Ket";
                else
                    donViTinh = value;
            }
        }
        public int soLuong;
        public float donGia;
        public static double chietKhau = 0.1;
        public nuocGiaiKhat() : base()
        {
            dvt = "Ket";
            soLuong = 0;
            donGia = 0;
        }
        public nuocGiaiKhat(string ma, string ten, string dv, int sl, float gia) : base(ma, ten)
        {
            dvt = dv;
            soLuong = sl;
            donGia = gia;
        }
        public double tongTien()
        {
            if (dvt == "Ket" || dvt == "Thung")
                return soLuong * donGia * chietKhau;
            else if (dvt == "Chai")
                return (soLuong * donGia / 20) * chietKhau;
            else if (dvt == "Lon")
                return (soLuong * donGia / 24) * chietKhau;
            return 0;

        }
        public override void nhap()
        {
            base.nhap();
            Console.WriteLine("Nhap don vi tinh:");
            dvt = Console.ReadLine();
            Console.WriteLine("Nhap so luong: ");
            soLuong = int.Parse(Console.ReadLine());
            Console.WriteLine("Nhap don gia: ");
            donGia = float.Parse(Console.ReadLine());
        }
        public override void xuat()
        {
            base.xuat();
            Console.WriteLine("So luong: {0}\tDon gia: {1}\tDon vi tinh:{2}\tTong tien: {3}", soLuong, donGia, dvt, tongTien());
        }

    }
}

