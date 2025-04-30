package com.expencetracker.api.auth.application.dto;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public record UserDto(

        @NotNull
        @Size(min = 3, max = 25)
        String names,

        @NotNull
        @Size(min = 6, max = 255)
        String passwords
) {
}
