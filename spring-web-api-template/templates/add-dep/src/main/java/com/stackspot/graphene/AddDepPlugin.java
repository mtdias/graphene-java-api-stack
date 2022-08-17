package com.stackspot.graphene;

import org.gradle.api.Plugin;
import org.gradle.api.Project;

public class AddDepPlugin implements Plugin<Project> {
    public void apply(Project project) {
        project.getTasks().register("addDep", AddDepTask.class, task -> {
            task.setGroup("StackSpot");
            task.setDescription("Add a dependency to build.gradle");
        });
    }
}
