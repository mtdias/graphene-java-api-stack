package com.stackspot.graphene;

import org.gradle.api.DefaultTask;
import org.gradle.api.tasks.TaskAction;
import org.gradle.api.tasks.options.Option;
import org.gradle.api.tasks.options.OptionValues;

import java.util.EnumSet;
import java.io.IOException;
import java.util.Collection;

public class AddDepTask extends DefaultTask {

    public enum Config {
        IMPLEMENTATION("implementation"),
        DEVELOPMENTONLY("developmentOnly"),
        TESTIMPLEMENTATION("testImplementation"),
        RUNTIMEONLY("runtimeOnly"),
        ANNOTATIONPROCESSOR("annotationProcessor");

        private final String name;

        Config(String name) {
            this.name = name;
        }

        public String getName() {
            return this.name;
        }
    }

    private Config config;

    private String dep;

    public AddDepTask() {
    }

    @Option(option = "dep", description = "The dependency to be added, in the format 'group:name:version:classifier@extension', in which all properties, except name, are optional")
    public void setDep(String dep) {
        this.dep = dep;
    }

    @Option(option = "config", description = "The Gradle configuration name")
    public void setConfig(Config config) {
        this.config = config;
    }

    @OptionValues("config")
    Collection<Config> getSupportedConfigs() {
        return EnumSet.allOf(Config.class);
    }

    @TaskAction
    public void addDep() throws IOException {
        getProject().getDependencies().add(config.getName(), dep);
    }
}
