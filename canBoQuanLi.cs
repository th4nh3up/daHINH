using System;
namespace canbo
{
	public class canBoQuanLi:nhanVien
	{
		public string chucVu;
		public int thamNien;
		public canBoQuanLi():base()
		{
			ma = "NV009";
			tenNV = "Dieu Hien";
			heSoLuong = 4.67;
			chucVu = "Giam doc";
			thamNien = 10;
		}
		public double phuCapLanhDao()
		{
			if (chucVu == "Giam doc")
				return 1500 * 7.0;
			if (chucVu == "Truong phong")
				return 1500 * 6.0;
			if (chucVu == "Pho phong")
				return 1500 * 4.5;
			return 1500;
		}
        public override double thuNhap()
        {
			return base.thuNhap() + phuCapLanhDao();
        }
        public override void xuat()
        {
			Console.Write("\n");
            base.xuat();
			Console.Write("\t{0}\t{1}", chucVu, thamNien);
        }

    }
}

