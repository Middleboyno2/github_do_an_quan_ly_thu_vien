public class KySu extends CanBo{
    //Thuộc tính
    private String nganh;


    public KySu(String ten, int tuoi, String gioiTinh, String que,String nganh) {
        super(ten, tuoi, gioiTinh, que);
        this.nganh=nganh;
    }
    //get set

    public String getNganh() {
        return nganh;
    }

    public void setNganh(String nganh) {
        this.nganh = nganh;
    }

    @Override
    public void hienThi(){
        super.hienThi();
        System.out.print(nganh);
   
}
