package com.stackspot.graphene;

import org.gradle.api.DefaultTask;
import org.gradle.api.tasks.TaskAction;
import org.gradle.api.tasks.options.Option;
import org.gradle.api.tasks.options.OptionValues;

import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class AddDepTask extends DefaultTask {

    private final BuildFileEditor buildFileEditor = new BuildFileEditor();

    private final DepAnalyzer depAnalyzer = new DepAnalyzer();

    private MacroDep dep;

    public AddDepTask() {
    }

    @Option(option = "dep", description = "The dependency to be added")
    public void setDep(MacroDep dep) {
        this.dep = dep;
    }

    @OptionValues("dep")
    Collection<MacroDep> getSupportedDeps() {
        return EnumSet.allOf(MacroDep.class);
    }

    @TaskAction
    public void addDep() throws IOException {
        buildFileEditor.addMonoDeps(
                getProject().getBuildFile().toPath(),
                depAnalyzer.getMissingMonoDeps(getProject(), dep)
        );
    }


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

    public enum MacroDep {
        SPRING_ACTUATOR(
                new MonoDep[] {
                        new MonoDep(
                                Config.IMPLEMENTATION,
                                "org.springframework.boot:spring-boot-starter-actuator"
                        )
                }
        );

        private final Set<MonoDep> deps = new HashSet<>();

        MacroDep(MonoDep[] deps) {
            this.deps.addAll(Arrays.stream(deps).collect(Collectors.toList()));
        }

        public Set<MonoDep> getDeps() {
            return new HashSet<>(deps);
        }
    }

    public static class MonoDep {
        private final Config config;

        // should always have at least 'group:name'
        private final String notation;

        public MonoDep(
                Config config,
                String notation
        ) {
            this.config = config;
            this.notation = notation;
        }

        public Config getConfig() {
            return config;
        }

        public String getNotation() {
            return notation;
        }

        public String getGroup() {
            return notation.split(":")[0];
        }

        public String getName() {
            return notation.split(":")[1];
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            MonoDep that = (MonoDep) o;
            return config == that.config && Objects.equals(notation, that.notation);
        }

        @Override
        public int hashCode() {
            return Objects.hash(config, notation);
        }
    }
}
