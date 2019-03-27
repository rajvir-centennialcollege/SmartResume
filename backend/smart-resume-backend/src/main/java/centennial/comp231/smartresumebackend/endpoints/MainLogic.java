package centennial.comp231.smartresumebackend.endpoints;

import centennial.comp231.smartresumebackend.POJO.CandidateProfile;
import centennial.comp231.smartresumebackend.POJO.RegistrationInfo;
import centennial.comp231.smartresumebackend.POJO.Response;
import com.google.gson.Gson;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class MainLogic {

    Map<String, RegistrationInfo> userMap = new HashMap<>();
    Map<String, CandidateProfile> candidateProfileMap = new HashMap<>();
    Gson gson = new Gson();

    @RequestMapping(value = "/candidateregister", method = RequestMethod.POST)
    public String registerCandidate(@RequestBody String payload) {
        RegistrationInfo registrationInfo = gson.fromJson(payload, RegistrationInfo.class);
        if (userMap.containsKey(registrationInfo.getEmail())) {
            Response response = new Response(null, "User: " + registrationInfo.getEmail() + " already registered. Please use reset password if you forgot your password");
            return gson.toJson(response);
        } else {
            userMap.put(registrationInfo.getEmail(), registrationInfo);
            Response response = new Response(registrationInfo, "Registration Successful!");
            return gson.toJson(response);
        }
    }

    @RequestMapping(value = "/candidatelogin", method = RequestMethod.POST)
    public String loginCandidate(@RequestBody String payload) {
        RegistrationInfo loginInfo = gson.fromJson(payload, RegistrationInfo.class);
        if (userMap.containsKey(loginInfo.getEmail())) {
            RegistrationInfo user = userMap.get(loginInfo.getEmail());
            if (user.getPassword().equals(loginInfo.getPassword())) {
                Response response = new Response(null, "User: " + loginInfo.getEmail() + " login successful.");
                return gson.toJson(response);
            } else {
                Response response = new Response(null, "User: " + loginInfo.getEmail() + " provided incorrect password.");
                return gson.toJson(response);
            }
        } else {
            Response response = new Response(null, "User: " + loginInfo.getEmail() + " is not registered. Please use Sign Up to register first.");
            return gson.toJson(response);
        }
    }

    @RequestMapping(value = "/deleteaccount", method = RequestMethod.DELETE)
    public String deleteAccount(@RequestBody String payload) {
        RegistrationInfo deleteAcc = gson.fromJson(payload, RegistrationInfo.class);
        if (userMap.containsKey(deleteAcc.getEmail())) {
            userMap.remove(deleteAcc.getEmail());
            Response response = new Response(null, "User: " + deleteAcc.getEmail() + " has been deleted.");
            return gson.toJson(response);
        } else {
            Response response = new Response(null, "User: " + deleteAcc.getEmail() + " is not registered.");
            return gson.toJson(response);
        }
    }

    @RequestMapping(value = "/updatepassword", method = RequestMethod.PUT)
    public String updatePassword(@RequestBody String payload) {
        RegistrationInfo updatePass = gson.fromJson(payload, RegistrationInfo.class);
        if (userMap.containsKey(updatePass.getEmail())) {
            RegistrationInfo registrationInfo = userMap.get(updatePass.getEmail());
            registrationInfo.setPassword(updatePass.getPassword());
            userMap.remove(updatePass.getEmail());
            userMap.put(registrationInfo.getEmail(), registrationInfo);
            Response response = new Response(userMap.get(updatePass.getEmail()), "Password updated successfully!");
            return gson.toJson(response);
        } else {
            Response response = new Response(null, "User: " + updatePass.getEmail() + " is not registered.");
            return gson.toJson(response);
        }
    }

    @RequestMapping(value = "/updateProfile", method = RequestMethod.POST)
    public String updateProfile(@RequestBody String payload) {
        RegistrationInfo registrationInfo = gson.fromJson(payload, RegistrationInfo.class);
        CandidateProfile candidateProfile = gson.fromJson(payload, CandidateProfile.class);
        if (userMap.containsKey(registrationInfo.getEmail())) {
            candidateProfileMap.put(registrationInfo.getEmail(), candidateProfile);
            Response response = new Response(candidateProfileMap.get(registrationInfo.getEmail()), "User: " + registrationInfo.getEmail() + "'s profile registered.");
            return gson.toJson(response);
        } else {
            Response response = new Response(null, "User: " + registrationInfo.getEmail() + " is not registered.");
            return gson.toJson(response);
        }
    }

    @RequestMapping(value = "/getprofile", method = RequestMethod.GET)
    public String getProfile(@RequestBody String payload) {
        RegistrationInfo registrationInfo = gson.fromJson(payload, RegistrationInfo.class);
        if (userMap.containsKey(registrationInfo.getEmail())) {
            if (candidateProfileMap.containsKey(registrationInfo.getEmail())) {
                Response response = new Response(candidateProfileMap.get(registrationInfo.getEmail()), null);
                return gson.toJson(response);
            } else {
                Response response = new Response(null, "User: " + registrationInfo.getEmail() + "'s profile is not recorded.");
                return gson.toJson(response);
            }
        } else {
            Response response = new Response(null, "User: " + registrationInfo.getEmail() + " is not registered.");
            return gson.toJson(response);
        }
    }

}
