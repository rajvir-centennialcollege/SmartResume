package centennial.comp231.smartresumebackend.POJO;

import com.google.gson.Gson;

import java.io.File;

public class CandidateProfile {

    private String name;
    private String address;
    private String phone;
    private String resumeLink;

    public CandidateProfile() {
        this.name = "";
        this.address = "";
        this.phone = "";
        this.resumeLink = null;
    }

    public CandidateProfile(String name, String address, String phone, String resumeLink) {
        this.name = name;
        this.address = address;
        this.phone = phone;
        this.resumeLink = resumeLink;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getResumeLink() {
        return resumeLink;
    }

    public void setResumeLink(String resumeLink) {
        this.resumeLink = resumeLink;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        CandidateProfile that = (CandidateProfile) o;

        if (name != null ? !name.equals(that.name) : that.name != null) return false;
        if (address != null ? !address.equals(that.address) : that.address != null) return false;
        if (phone != null ? !phone.equals(that.phone) : that.phone != null) return false;
        return resumeLink != null ? resumeLink.equals(that.resumeLink) : that.resumeLink == null;
    }

    @Override
    public int hashCode() {
        int result = name != null ? name.hashCode() : 0;
        result = 31 * result + (address != null ? address.hashCode() : 0);
        result = 31 * result + (phone != null ? phone.hashCode() : 0);
        result = 31 * result + (resumeLink != null ? resumeLink.hashCode() : 0);
        return result;
    }

    @Override
    public String toString() {
        return new Gson().toJson(this);
    }
}
