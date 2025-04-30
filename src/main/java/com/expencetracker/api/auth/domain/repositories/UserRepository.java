package com.expencetracker.api.auth.domain.repositories;

import com.expencetracker.api.auth.domain.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
