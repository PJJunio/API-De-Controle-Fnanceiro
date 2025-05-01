package com.expencetracker.api.auth.domain.repositories;

import com.expencetracker.api.auth.domain.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;
import java.util.UUID;

public interface UserRepository extends JpaRepository<User, UUID> {
    Optional<User> findByExternalId(UUID externalId);
}
