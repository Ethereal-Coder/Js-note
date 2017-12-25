package com.deepbay.microserver.wxbot.models;

/**
 * Created by deepbay on 2017/12/12.
 */

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.io.Serializable;

@Getter @Setter
@Entity
@Table(name = "wx_container")
public class WxContainer implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String name;
    private String wxid;
    private String containerId;
    private String containerState;

}
