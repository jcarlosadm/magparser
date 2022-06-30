package com.jcarlosadm.magparser;

import com.jcarlosadm.magparser.htmlparser.Topic;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class MagazineAPI {

    @GetMapping("/api/get_topics")
    public List<Topic> getTopics(){
        // TODO: implement it
        return new ArrayList<>();
    }
}
