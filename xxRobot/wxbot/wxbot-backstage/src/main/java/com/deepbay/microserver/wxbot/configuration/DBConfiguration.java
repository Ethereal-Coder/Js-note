package com.deepbay.microserver.wxbot.configuration;

import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

/**
 * Created by deepbay on 2017/12/12.
 */
@Configuration
@EntityScan(basePackages = "com.deepbay.microserver.wxbot.models")
@EnableJpaRepositories(basePackages = "com.deepbay.microserver.wxbot.repositories")
public class DBConfiguration {
}
