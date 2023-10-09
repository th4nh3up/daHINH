using System;
namespace sinhVien
{
	public class sinhVien:nguoi
	{
		public string maSV;
		string heDaoTao;
		public string he
		{
			get { return heDaoTao; }
			set
			{
				if (value != "Dai hoc" || value != "Cao dang" || value != "Cao dang nghe")
					heDaoTao = "Dai hoc";
				else
					heDaoTao = value;
			}
		}
		public sinhVien(string ten, string ns, string gtinh, string ma, string hedaotao):base(ten,ns,gtinh)
		{
			maSV = ma;
			heDaoTao = hedaotao;
		}
		public int soTC()
		{
			if (he == "Dai hoc")
				return 150;
			else if (he == "Cao dang")
				return 100;
			return 130;
		}
		public int tongTien()
		{
            if (he == "Dai hoc")
                return 150 * 200000;
            else if (he == "Cao dang")
                return 100* 150000;
            return 130 * 120000;
        }
        public override void xuat()
        {
			Console.Write("\n");
            base.xuat();
			Console.Write("{0}\t{1}\t{2}\t{3}", maSV, he, soTC(), tongTien());
        }

    }
}

