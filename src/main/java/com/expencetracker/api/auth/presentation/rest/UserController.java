package com.expencetracker.api.auth.presentation.rest;

import com.expencetracker.api.auth.application.dto.ListUsersDto;
import com.expencetracker.api.auth.application.dto.UserDto;
import com.expencetracker.api.auth.domain.model.User;
import com.expencetracker.api.auth.domain.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/user")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @PostMapping
    @Transactional
    public void cadastraUser(@RequestBody UserDto userDto) {
        var user = new User(userDto);
        userRepository.save(user);
    }

    @PostMapping
    @Transactional
    @RequestMapping("/list")
    public Page<ListUsersDto> listUsers(@PageableDefault(size = 10, sort = {"names"}) Pageable paginacao) {
        return userRepository.findAll(paginacao).map(ListUsersDto::new);
    }
}
