package com.expencetracker.api.auth.application.dto;

import com.expencetracker.api.auth.domain.model.User;

public record ListUsersDto(Long users_ids, String names, String passwords) {

    public ListUsersDto (User user) {
        this(user.getId(), user.getNames(), user.getPasswords());
    }
}
