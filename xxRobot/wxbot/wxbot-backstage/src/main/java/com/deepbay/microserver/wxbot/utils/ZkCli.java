package com.deepbay.microserver.wxbot.utils;

import lombok.extern.slf4j.Slf4j;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.framework.recipes.cache.ChildData;
import org.apache.curator.framework.recipes.cache.TreeCache;
import org.apache.curator.framework.recipes.cache.TreeCacheEvent;
import org.apache.curator.framework.recipes.cache.TreeCacheListener;
import org.apache.curator.retry.RetryNTimes;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Created by deepbay on 2017/12/12.
 */
@Slf4j
public class ZkCli {

    public static String WX_NODE_PATH = "/deepbay/wx";
    public static String WX_THE_NODE_PATH = WX_NODE_PATH + "/nodes";
    public static String WX_COMMAND_PATH = WX_NODE_PATH + "/commands";
    public static String WX_PICTURE_PATH = WX_NODE_PATH + "/images";

    private static final String ZK_ADDRESS = "192.168.1.155:2181";
    private static final String ZK_PATH = "/zktest";

    private static CuratorFramework client;

    static {
        client = CuratorFrameworkFactory.newClient(
                ZK_ADDRESS,
                new RetryNTimes(10, 5000)
        );
        client.start();

        listenNodes();
    }

    public static String  getData(String path) {
        try {
            byte[] data = client.getData().forPath(path);
            return new String(data);
        }catch (Exception e){
            log.debug("get data for path ==> " + path ,e);
            return "";
        }
    }

    private static void listenNodes(){
        ExecutorService pool = Executors.newCachedThreadPool();
        //设置节点的cache
        TreeCache treeCache = new TreeCache(client, WX_THE_NODE_PATH);
        //设置监听器和处理过程
        treeCache.getListenable().addListener(new TreeCacheListener() {
            @Override
            public void childEvent(CuratorFramework client, TreeCacheEvent event) throws Exception {
                ChildData data = event.getData();
                if(data !=null){
                    switch (event.getType()) {
                        case NODE_ADDED:
                            System.out.println("NODE_ADDED : "+ data.getPath() +"  数据:"+ new String(data.getData()));
                            break;
                        case NODE_REMOVED:
                            String uuid = data.getPath().substring(WX_THE_NODE_PATH.length()+1);
                            log.info("remove uuid is "+uuid);
                            DockerBuilder.build().removeApp(uuid);
                            System.out.println("NODE_REMOVED : "+ data.getPath() +"  数据:"+ new String(data.getData()));
                            break;
                        case NODE_UPDATED:
                            System.out.println("NODE_UPDATED : "+ data.getPath() +"  数据:"+ new String(data.getData()));
                            break;

                        default:
                            break;
                    }
                }else{
                    System.out.println( "data is null : "+ event.getType());
                }
            }
        });
        try {
            //开始监听
            treeCache.start();
        }catch (Exception e){
            e.printStackTrace();
        }
    }


}
