using System;
namespace canbo
{
	public class nhanVien
	{
		 string maNV;
		public string tenNV;
		public double heSoLuong;
		static public int LCB = 1150;
		public string ma
		{
			get { return maNV; }
			set {
				if (!value.StartsWith("NV") && value.Length != 6)
					maNV = "NV001";
				else
					maNV = value;
			}

		}

		public nhanVien()
		{
			ma = "NV001";
			tenNV = "Le Dinh Thanh Hung";
			heSoLuong = 2.34;
		}
		public nhanVien(string m, string ten, double hsl)
		{
			ma = m;
			tenNV = ten;
			heSoLuong = hsl;
		}
		public virtual double thuNhap()
		{
			return heSoLuong * LCB;
		}
		public virtual void xuat()
		{
			Console.Write("{0}\t{1}\t{2}\t", ma, tenNV,thuNhap());
		}


	}
}

