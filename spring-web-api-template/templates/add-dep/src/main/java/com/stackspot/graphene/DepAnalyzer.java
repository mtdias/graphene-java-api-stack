package com.stackspot.graphene;

import org.gradle.api.Project;

import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;

public class DepAnalyzer {

    public Set<AddDepTask.MonoDep> getMissingMonoDeps(Project project, AddDepTask.MacroDep macroDep) {
        final var presentDeps =
                project.getConfigurations().getAsMap().values()
                        .stream()
                        .flatMap(
                                config -> config.getDependencies().stream()
                        ).collect(Collectors.toSet());

        return macroDep.getDeps()
                .stream()
                .filter(
                        requiredMonoRep -> presentDeps.stream().noneMatch(
                            presentDep ->
                                    Objects.requireNonNullElse(
                                            presentDep.getGroup(),
                                            requiredMonoRep.getGroup()
                                    ).equalsIgnoreCase(requiredMonoRep.getGroup())
                                            && presentDep.getName().equalsIgnoreCase(requiredMonoRep.getName())
                        )
                ).collect(Collectors.toSet());
    }
}
