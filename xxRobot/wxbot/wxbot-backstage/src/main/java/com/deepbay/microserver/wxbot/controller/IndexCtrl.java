package com.deepbay.microserver.wxbot.controller;

import com.deepbay.alphatao.common.request.ApiRequest;
import com.deepbay.alphatao.common.request.Query;
import com.deepbay.alphatao.common.request.RequestData;
import mesosphere.marathon.client.Marathon;
import mesosphere.marathon.client.MarathonClient;
import mesosphere.marathon.client.model.v2.App;
import mesosphere.marathon.client.model.v2.Container;
import mesosphere.marathon.client.model.v2.Docker;
import mesosphere.marathon.client.model.v2.Network;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;
import java.util.*;

/**
 * Created by xizil on 16/10/10.
 */

@Controller
public class IndexCtrl {

//    @RequestMapping("/api/search")
//    @ResponseBody
//    public RequestData index(Model model) {
//        model.addAttribute("string", "bootstrap");
//        RequestData data = null;
//        try {
//            data = ApiRequest.callGroup(Query.buildGroupTextQuery().addKeyword("牛奶"),null);
//
//            System.out.println(data);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        return data;
//    }

    @RequestMapping("/home")
    public String home(Model model) {
        model.addAttribute("string", "bootstrap");
        return "home";
    }

    @RequestMapping("/index")
    public String index(Model model) {
        model.addAttribute("string", "bootstrap");
        return "index";
    }


    /**
     * 创建Docker
     * @return
     */
    @GetMapping("/createDocker")
    @ResponseBody
    public String createDocker(){
        String uuid = UUID.randomUUID().toString();

        Marathon marathon = MarathonClient.getInstance("http://192.168.1.133:8080");
        App app = new App();
        app.setId("wxbot/"+uuid);
        app.setInstances(1);
        app.setCpus(0.2);
        app.setMem(200d);


        Map<String,Object> envs = new HashMap<>();
        envs.put("UUID", uuid);
        app.setEnv(envs);

        Container container = new Container();

        Docker docker = new Docker();
        docker.setImage("com.deepbay/wxbot:latest");
        docker.setNetwork("HOST");
        docker.setForcePullImage(true);
        container.setDocker(docker);


        app.setContainer(container);
        marathon.createApp(app);
        return "success";
    }
}
