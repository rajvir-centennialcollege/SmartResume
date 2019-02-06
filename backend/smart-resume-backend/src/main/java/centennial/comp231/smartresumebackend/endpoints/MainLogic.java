package centennial.comp231.smartresumebackend.endpoints;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainLogic {

    @RequestMapping(value = "/candidateregister", method = RequestMethod.POST)
    public String registerCandidate(){
        return "Registered";
    }

}
