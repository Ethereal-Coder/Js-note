package com.deepbay.microserver.wxbot.repositories;

import com.deepbay.microserver.wxbot.models.WxContainer;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * Created by deepbay on 2017/12/12.
 */
public interface WxContainerDao extends JpaRepository<WxContainer,Integer> {
}
