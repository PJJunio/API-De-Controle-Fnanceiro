package com.expencetracker.api.auth.domain.model;

import com.expencetracker.api.auth.application.dto.UserDto;
import jakarta.persistence.*;
import lombok.*;

import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity(name = "User")
@Table(name = "users")
@EqualsAndHashCode(of = "externalId")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "users_ids")
    private Long id;

    @Column(name = "external_id", nullable = false, updatable = false)
    private UUID externalId;

    @Column(name = "usernames", unique = true, nullable = false)
    private String names;

    @Column(name = "passwords", nullable = false)
    private String passwords;

    private int attempts = 0;
    private boolean account_locked = false;

    public User(UserDto userDto) {
        this.names = userDto.names();
        this.passwords = userDto.passwords();
        this.externalId = UUID.randomUUID();
    }

    public void attempts() {
        this.attempts++;
        if (attempts > 5) {
            account_locked = true;
        }
    }

    public void resetAttempts() {
        this.attempts = 0;
        this.account_locked = false;
    }
}

