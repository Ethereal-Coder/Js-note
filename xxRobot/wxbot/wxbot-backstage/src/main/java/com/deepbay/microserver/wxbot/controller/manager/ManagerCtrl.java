package com.deepbay.microserver.wxbot.controller.manager;

import com.deepbay.microserver.wxbot.models.WxContainer;
import com.deepbay.microserver.wxbot.repositories.WxContainerDao;
import com.deepbay.microserver.wxbot.utils.DockerBuilder;
import com.deepbay.microserver.wxbot.utils.ZkCli;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

/**
 * Created by deepbay on 2017/12/12.
 */
@Controller
@RequestMapping("/manager")
public class ManagerCtrl {

    @Autowired
    private WxContainerDao wxContainerDao;

    @PostMapping("/createDocker")
    @ResponseBody
    public String createContainer(@ModelAttribute WxContainer container){
        Assert.notNull(container.getName(),"name can not be null.");


        String uuid = UUID.randomUUID().toString();
        DockerBuilder.build().createApp(uuid);
        container.setContainerId(uuid);

        wxContainerDao.save(container);
        return uuid;
    }

    @RequestMapping("/container_add")
    public String containerAdd(Model model){
        return "manager/container";
    }


    @GetMapping("/getImageData")
    @ResponseBody
    public String getImageData(String uuid){
        return ZkCli.getData(ZkCli.WX_PICTURE_PATH+"/"+uuid);
    }

}
