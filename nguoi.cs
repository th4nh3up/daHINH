using System;
namespace sinhVien
{
	public class nguoi
	{
		public string hoTen;
		public string ngaySinh;
		string gioiTinh;
		public string gt
		{
			get { return gioiTinh; }
			set
			{
				if (value != "nam" || value != "nu")
					gioiTinh = "nam";
				else
					gioiTinh = value;
			}
		}
		public nguoi()
		{
			hoTen = "Le Dinh Thanh Hung";
			ngaySinh = "17/01/2004";
			gt = "nam";
		}
		public nguoi(string ten, string ns, string gtinh)
		{
			hoTen = ten;
			ngaySinh = ns;
			gioiTinh = gtinh;
		}
		public virtual void xuat()
		{
			Console.Write("{0}\t{1}\t{2}\t", hoTen, ngaySinh, gt);
		}
	}
}

