package com.deepbay.microserver.wxbot.utils;

import mesosphere.marathon.client.Marathon;
import mesosphere.marathon.client.MarathonClient;
import mesosphere.marathon.client.model.v2.App;
import mesosphere.marathon.client.model.v2.Container;
import mesosphere.marathon.client.model.v2.Docker;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by deepbay on 2017/12/12.
 */
public class DockerBuilder {

    private final static String MARATHON_MANAGER_URL = "http://192.168.1.133:8080";
    private final static String WX_APP_ID_PREFIX = "wxbot/";

    private Marathon marathon;

    private DockerBuilder(){
        marathon = MarathonClient.getInstance(MARATHON_MANAGER_URL);
    }

    public static DockerBuilder build(){
        return new DockerBuilder();
    }

    public void createApp(String uuid){
        App app = new App();
        app.setId(WX_APP_ID_PREFIX+uuid);
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
    }


    public void removeApp(String uuid){
        marathon.deleteApp(WX_APP_ID_PREFIX+uuid);
    }





}
