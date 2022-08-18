package com.stackspot.graphene;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Set;
import java.util.regex.Pattern;

public class BuildFileEditor {

    private static final Pattern GRADLE_DEPENDENCIES_PATTERN = Pattern.compile("(\\s*dependencies\\s*\\{)\n*");

    public void addMonoDeps(Path buildFilePath, Set<AddDepTask.MonoDep> monoDeps) throws IOException {
        var buildFileContent =
                Files.readAllLines(buildFilePath, Charset.defaultCharset())
                        .stream()
                        .reduce(
                                "",
                                (partialString , element) -> partialString + element + "\n"
                        );

        buildFileContent = GRADLE_DEPENDENCIES_PATTERN.matcher(buildFileContent).replaceFirst(
                "$1\n" +
                        monoDeps.stream().map(
                                monoDep -> "\t" + monoDep.getConfig().getName() + " '" + monoDep.getNotation() + "'\n"
                        ).reduce(
                                "",
                                (partialString , element) -> partialString + element
                        )
        );

        Files.writeString(buildFilePath, buildFileContent);
    }
}
